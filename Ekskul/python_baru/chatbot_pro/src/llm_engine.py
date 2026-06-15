from groq import Groq
import streamlit as st

# --- KONFIGURASI MODEL ---
MODEL_VISION = "meta-llama/llama-4-maverick-17b-128e-instruct" 
MODEL_TEXT_MAIN = "llama-3.3-70b-versatile"
MODEL_TEXT_BACKUP = "llama-3.1-8b-instant"

def get_client():
    """Initializes and returns the Groq client using secrets."""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except FileNotFoundError:
        st.error("Secrets file not found. Please create .streamlit/secrets.toml")
        return None
    
    return Groq(
        api_key=api_key
    )

def generate_answer(history, model_list, custom_instruction=None):
    """
    Generates an answer using the provided model list with fallback support.
    """
    client = get_client()
    if not client:
        return "System Error: API Key missing.", "Error"

    base_instruction = (
        "You are an expert AI assistant. "
        "For coding questions, provide clean, efficient, and commented code. "
        "For document analysis, be precise and cite the text provided. "
        "If the user speaks Indonesian, reply in Indonesian."
    )

    # Inject custom instruction if exists
    final_instruction = f"{base_instruction}\n\n[USER CUSTOM INSTRUCTION]: {custom_instruction}" if custom_instruction else base_instruction

    system_prompt = {
        "role": "system", 
        "content": final_instruction
    }
    
    messages_to_send = [system_prompt] + history
    last_error = None
    
    for model_id in model_list:
        try:
            # Vision models usually need fewer output tokens to avoid timeouts
            # Check for vision-capable model names
            is_vision_capable = any(kw in model_id.lower() for kw in ["vision", "maverick", "scout", "llama-4"])
            max_tok = 1024 if is_vision_capable or "11b" in model_id else 4096
            print(f"Trying model: {model_id}")
            
            stream = client.chat.completions.create(
                model=model_id,
                messages=messages_to_send,
                temperature=1,
                max_tokens=max_tok,
                stream=True,  # ENABLE STREAMING
                stop=None
            )
            
            # Wrapper to extract text for st.write_stream
            def content_generator():
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content

            used_model = model_id
            return content_generator(), used_model
            
        except Exception as e:
            last_error = e
            print(f"Model {model_id} failed: {e}. Switching to backup...")
            continue 
            
    # If all fail, return a generator that yields the error message
    def error_generator():
        yield f"Maaf, semua model sedang sibuk atau error. Detail: {last_error}"
    return error_generator(), "Error"
