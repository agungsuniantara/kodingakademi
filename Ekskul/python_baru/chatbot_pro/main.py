import streamlit as st
from datetime import datetime
from io import BytesIO

# Import modules
# from src.auth import auth_page
from src.database import init_db, check_usage_limit, increment_usage, get_user_subscription
from src.llm_engine import generate_answer, MODEL_VISION, MODEL_TEXT_MAIN, MODEL_TEXT_BACKUP
from src.utils import (
    encode_image, extract_text_from_pdf, get_smart_pdf_context,
    extract_text_from_docx, extract_text_from_csv, extract_text_from_xlsx,
    extract_text_from_html, extract_text_from_json
)

# --- CONFIGURATION ---
st.set_page_config(page_title="Pro Chatbot SaaS", page_icon="🚀", layout="wide")

# Load CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Init Database
init_db()

# --- PERSISTENT LOGIN VIA QUERY PARAMS ---
# (More reliable than cookies in Streamlit)

# --- SESSION STATE WITH QUERY PARAM RESTORE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "username" not in st.session_state:
    # Try to restore from URL query params first
    query_params = st.query_params
    if "user" in query_params:
        st.session_state.username = query_params["user"]
        st.session_state.logged_in = True
    else:
        # AUTO-GUEST LOGIN
        import uuid
        st.session_state.username = f"Guest_{str(uuid.uuid4())[:4]}"
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {"Chat 1": []}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Chat 1"

# --- LOGIN DIALOG ---
@st.dialog("🔐 Login / Register")
def login_dialog():
    from src.database import login_user, add_user
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login", use_container_width=True):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.chat_history = {"Chat 1": []} # Reset chat for new user
                # Save to URL for persistent login
                st.query_params["user"] = username
                st.rerun()
            else:
                st.error("Invalid credentials")
                
    with tab2:
        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register", use_container_width=True):
            if new_pass and add_user(new_user, new_pass):
                st.success("Created! Please login.")
            else:
                st.error("Error creating account")

# --- MAIN FLOW ---
# (No User Blocking anymore)
username = st.session_state.username
subscription = get_user_subscription(username) # Guest is 'free' by default

# Sidebar
st.sidebar.title(f"👤 {username}")
st.sidebar.caption(f"Plan: {subscription.upper()}")

# Usage Progress Bar
from src.database import get_usage_count, get_all_users, update_user_subscription, get_user_settings, update_user_settings
usage_placeholder = st.sidebar.empty()

def render_usage_bar(current, limit, sub_status):
    with usage_placeholder.container():
        if sub_status == "free":
            st.progress(min(current / limit, 1.0))
            st.caption(f"Usage: {current}/{limit}")
        else:
            st.empty()

current_usage = get_usage_count(username)
limit = 5 if subscription == "free" else 100
render_usage_bar(current_usage, limit, subscription)

# --- UPGRADE BUTTON (Top of Sidebar) ---
@st.dialog("🚀 Upgrade to Premium")
def payment_dialog():
    st.write("Unlock unlimited messages, vision capabilities, and priority support.")
    st.markdown("""
    <div class="pricing-card" style="border: 2px solid #2563EB; background: #EFF6FF; padding: 1rem; margin-bottom: 1rem;">
        <span class="pricing-title" style="font-size: 1.2rem;">Premium Plan</span>
        <span class="pricing-price" style="font-size: 2rem;">$9.99</span>
        <div style="text-align: left; color: #475569; font-size: 0.9rem;">
            ✓ Unlimited Messaging<br>
            ✓ Vision & File Analysis<br>
            ✓ Priority Execution
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Select Payment Method:")
    st.selectbox("Card Type", ["Visa", "MasterCard", "PayPal"], label_visibility="collapsed")
    
    if st.button("Pay Now $9.99", type="primary", use_container_width=True):
         with st.spinner("Processing secure payment..."):
            import time
            time.sleep(2)
            update_user_subscription(username, "premium")
            st.session_state["upgrade_success"] = True
            st.rerun()

if subscription == "free":
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("💎 Upgrade Plan", type="primary", use_container_width=True):
        payment_dialog()

if st.session_state.get("upgrade_success", False):
    st.toast("Upgrade Successful! Welcome to Premium.", icon="🎉")
    st.session_state["upgrade_success"] = False # Reset

st.sidebar.divider()

# --- CHAT HISTORY (Below Divider) ---
col_c1, col_c2 = st.sidebar.columns([0.8, 0.2])
col_c1.subheader("Chats")
if col_c2.button("➕"):
    new_id = f"Chat {len(st.session_state.chat_history) + 1}"
    st.session_state.chat_history[new_id] = []
    st.session_state.current_chat_id = new_id
    st.rerun()

for chat_id in st.session_state.chat_history:
    if st.sidebar.button(chat_id, key=chat_id, use_container_width=True):
        st.session_state.current_chat_id = chat_id

st.sidebar.divider()

# --- ADMIN & SETTINGS (Bottom of Sidebar) ---
if username == "admin":
    with st.sidebar.expander("👮‍♂️ Admin Panel"):
        users = get_all_users()
        st.write(f"Total Users: {len(users)}")
        
        # User Management
        user_list = [u[0] for u in users]
        selected_user = st.selectbox("Select User", user_list)
        
        # Find status
        current_status = next((u[1] for u in users if u[0] == selected_user), "free")
        new_status = st.selectbox("Status", ["free", "premium"], index=0 if current_status == "free" else 1)
        
        if st.button("Update Status"):
            update_user_subscription(selected_user, new_status)
            st.success(f"Updated {selected_user} to {new_status}")
            st.rerun()

# --- SETTINGS ---
with st.sidebar.expander("⚙️ Settings"):
    current_instruction = get_user_settings(username) or ""
    new_instruction = st.text_area("Custom System Prompt", value=current_instruction, height=100, placeholder="E.g., Be concise.")
    if st.button("Save Settings"):
        update_user_settings(username, new_instruction)
        st.success("Saved!")

# --- LOGIN / LOGOUT ---
if st.session_state.logged_in:
    if st.sidebar.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        # Clear URL params for complete logout
        st.query_params.clear()
        del st.session_state.username # will trigger auto-guest on rerun
        st.rerun()
else:
    if st.sidebar.button("🔐 Login / Register", use_container_width=True):
        login_dialog()

# Chat Area
active_id = st.session_state.current_chat_id
col_header, col_export = st.columns([0.8, 0.2])

with col_export:
    # Export Chat functionality
    chat_text = ""
    for m in st.session_state.chat_history[active_id]:
        role = m["role"].upper()
        content = m["content"]
        if isinstance(content, list): content = "[Multi-modal Content]"
        chat_text += f"{role}: {content}\n\n"
        
    st.download_button(
        label="📥 Download",
        data=chat_text,
        file_name=f"{active_id}_history.txt",
        mime="text/plain"
    )

# --- HELPER: FILE PROCESSING ---
def process_file_batch(prompt, uploaded_files):
    """
    Processes a batch of uploaded files and returns API payload components.
    Returns: (api_content, memory_content, models_to_try, extra_metadata)
    """
    models_to_try = []
    api_content = prompt
    memory_content = prompt
    extra_metadata = {}

    if uploaded_files:
        # Store file objects for potential regeneration logic
        extra_metadata["uploaded_files_obj"] = uploaded_files
        
        # 1. Check for images to decide Model (robust: check MIME type AND extension)
        image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp")
        is_vision_task = any(
            ("image" in f.type) or f.name.lower().endswith(image_extensions)
            for f in uploaded_files
        )
        
        combined_text_context = ""
        image_contents = []
        display_names = [f.name for f in uploaded_files]
        
        # 2. Process all files
        for uploaded_file in uploaded_files:
            file_type = uploaded_file.type
            
            if file_type in ["image/png", "image/jpeg", "image/jpg", "image/gif", "image/webp"] or uploaded_file.name.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                base64_image = encode_image(uploaded_file)
                # GROQ/OpenAI requires Data URI format for local files
                mime_type = uploaded_file.type
                data_uri = f"data:{mime_type};base64,{base64_image}"
                image_contents.append(data_uri)
                extra_metadata.setdefault("display_images", []).append(uploaded_file)
                
            elif "pdf" in file_type:
                raw_text = extract_text_from_pdf(uploaded_file)
                smart_context = get_smart_pdf_context(raw_text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
            
            elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or uploaded_file.name.endswith(".docx"):
                raw_text = extract_text_from_docx(uploaded_file)
                smart_context = get_smart_pdf_context(raw_text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
            
            elif file_type == "text/csv" or uploaded_file.name.endswith(".csv"):
                raw_text = extract_text_from_csv(uploaded_file)
                smart_context = get_smart_pdf_context(raw_text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
            
            elif file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or uploaded_file.name.endswith(".xlsx"):
                raw_text = extract_text_from_xlsx(uploaded_file)
                smart_context = get_smart_pdf_context(raw_text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
            
            elif file_type == "text/html" or uploaded_file.name.endswith(".html"):
                raw_text = extract_text_from_html(uploaded_file)
                smart_context = get_smart_pdf_context(raw_text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
            
            elif file_type == "application/json" or uploaded_file.name.endswith(".json"):
                raw_text = extract_text_from_json(uploaded_file)
                smart_context = get_smart_pdf_context(raw_text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
            
            elif uploaded_file.name.endswith(".md"):
                # Markdown is plain text
                text = BytesIO(uploaded_file.getvalue()).read().decode("utf-8")
                smart_context = get_smart_pdf_context(text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"
                
            else: # txt and others
                text = BytesIO(uploaded_file.getvalue()).read().decode("utf-8")
                smart_context = get_smart_pdf_context(text, prompt)
                combined_text_context += f"\n--- File: {uploaded_file.name} ---\n{smart_context}\n"

        # 3. Construct Payload
        if is_vision_task:
            models_to_try = [MODEL_VISION]
            # PRIORITIZE QUESTION: Put question first, then context
            final_prompt = prompt
            if combined_text_context:
                 final_prompt = f"{prompt}\n\n[Additional Context from Text/PDF Files]:\n{combined_text_context}"
            
            # STRICT GROQ FORMAT: List of content parts
            # Part 1: Text
            api_content = [
                {
                    "type": "text", 
                    "text": final_prompt
                }
            ]
            
            # Part 2: Images
            # image_contents is expected to be a list of {"type": "image_url", "image_url": {"url": "data:image/..."}}
            # We explicitly verify/re-construct here to be safe
            for img in image_contents:
                if "image_url" in img:
                    api_content.append(img)
                else:
                    # Fallback if image_contents had just the url string (legacy)
                    api_content.append({
                        "type": "image_url",
                        "image_url": {"url": img}
                    })
            
            
            memory_content = api_content 
            
        else:
            models_to_try = [MODEL_TEXT_MAIN, MODEL_TEXT_BACKUP]
            full_prompt = f"Context:\n{combined_text_context}\n\nQuestion: {prompt}"
            api_content = full_prompt
            # For non-vision, Groq/OpenAI usually accepts string content too, 
            # but list structure is also valid. Sticking to string for text-only simplicity unless needed.
        
        extra_metadata["display_file_count"] = len(uploaded_files)
        extra_metadata["file_names"] = display_names

    else:
        models_to_try = [MODEL_TEXT_MAIN, MODEL_TEXT_BACKUP]
        
    return api_content, memory_content, models_to_try, extra_metadata


# --- EDIT DIALOG ---
@st.dialog("✏️ Edit Message")
def edit_dialog(index, current_text):
    new_text = st.text_area("Edit your message:", value=current_text, height=150)
    
    # NEW: File Upload in Edit Dialog
    active_hist = st.session_state.chat_history[active_id]
    msg = active_hist[index]
    
    # Check if there were previous files
    existing_files_info = ""
    if "file_names" in msg:
        existing_files_info = f"current attached: {', '.join(msg['file_names'])}"
    
    new_files = st.file_uploader(f"Replace attached files (Optional) {existing_files_info}", 
                                 type=["jpg", "png", "pdf", "txt", "docx", "csv", "xlsx", "html", "json", "md"], 
                                 accept_multiple_files=True,
                                 key=f"edit_upload_{index}")
                                 
    if st.button("Save & Regenerate", type="primary"):
        # 1. Start with the text update
        active_hist = st.session_state.chat_history[active_id]
        msg = active_hist[index]
        
        # 2. Logic: If NO new files, keep old files + new text.
        # If NEW files, REPLACE everything with new processing.
        
        if new_files:
             # Full replacement using helper
             api_c, mem_c, mods, meta = process_file_batch(new_text, new_files)
             msg["content"] = mem_c
             msg["api_payload"] = api_c
             msg.update(meta) # This updates file_names, display_images, etc.
             
        else:
            # Text Only Update (Keep existing files structure if any)
            # Complex case: modifying text in a Message that had images.
            if isinstance(msg["content"], str):
                 msg["content"] = new_text
                 msg["api_payload"] = new_text
            elif isinstance(msg["content"], list):
                 for part in msg["content"]:
                     if part["type"] == "text":
                         part["text"] = new_text
                 # If we had images, they persist in the list logic.
                 # Using the old api_payload which was likely constructed similarly.
                 # Note: If it was RAG (Text context from PDF), changing prompt 
                 # might ideally want to re-inject context. 
                 # But simplistic view: "content" holds the memory.
                 pass

        # 3. Truncate history
        st.session_state.chat_history[active_id] = active_hist[:index+1]
        
        # 4. Trigger Regeneration (with flag that we don't need to re-process files if we just did)
        st.session_state["generation_trigger"] = True
        st.rerun()

# Display History
if not st.session_state.chat_history[active_id]:
    # STARTER QUESTIONS (Centered)
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; margin-bottom: 30px;">
        <h2 style="color: #FFFFFF;">👋 How can I help you today?</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Suggestion Cards Removed by User Request
    pass

# Render Chat History with Edit Buttons
for i, msg in enumerate(st.session_state.chat_history[active_id]):
    with st.chat_message(msg["role"]):
        # User Message: Show Edit Button
        if msg["role"] == "user":
            c1, c2 = st.columns([0.9, 0.1])
            with c1:
                # Display Content
                if "file_names" in msg:
                    for fname in msg.get("file_names", []):
                        st.info(f"📎 {fname}")
                if "display_images" in msg:
                    for img in msg.get("display_images", []):
                        st.image(img, width=300)
                
                # Fallbacks
                if "display_file" in msg: st.info(f"📎 {msg['display_file']}")
                if "display_image" in msg: st.image(msg['display_image'], width=300)
                
                # Text Content extraction for display
                display_text = ""
                if isinstance(msg["content"], str):
                    display_text = msg["content"]
                elif isinstance(msg["content"], list):
                    for part in msg["content"]:
                        if part["type"] == "text":
                            display_text = part["text"]
                st.write(display_text)
            
            with c2:
                # Edit Button
                if st.button("✏️", key=f"edit_{i}", help="Edit message"):
                    # Extract text for the editor
                    text_for_edit = display_text
                    edit_dialog(i, text_for_edit)
                    
        else:
            # Assistant Message: Standard Display
            st.write(msg["content"])
            if "used_model" in msg:
                st.caption(f"⚡ {msg['used_model']}")

# Input Area
if "uploader_key" not in st.session_state:
    st.session_state["uploader_key"] = 0

with st.container():
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
            with st.popover("📎", use_container_width=True):
                uploaded_files = st.file_uploader(
                    "Upload", 
                    type=["jpg", "png", "pdf", "txt", "docx", "csv", "xlsx", "html", "json", "md"], 
                    accept_multiple_files=True, 
                    label_visibility="collapsed",
                    key=f"uploader_{st.session_state['uploader_key']}"
                )

# PROMPT PROCESSING
user_input = st.chat_input("Message...")

if "suggested_prompt" in st.session_state:
    user_input = st.session_state.pop("suggested_prompt")

# 1. HANDLE NEW INPUT OR REGENERATION
if user_input or st.session_state.get("generation_trigger"):
    
    # Capture state for later use
    is_regeneration = st.session_state.get("generation_trigger", False)
    
    # Reset trigger if it was set
    if is_regeneration:
        st.session_state["generation_trigger"] = False
        # For regeneration, the prompt is the last user message in history
        last_user_msg = st.session_state.chat_history[active_id][-1]
        if isinstance(last_user_msg["content"], str):
            prompt = last_user_msg["content"]
        elif isinstance(last_user_msg["content"], list):
            # Extract text from multi-modal content
            prompt = ""
            for part in last_user_msg["content"]:
                if part["type"] == "text":
                    prompt = part["text"]
                    break
        # Also retrieve files if they were part of the original message
        uploaded_files = last_user_msg.get("uploaded_files_obj", []) # Assuming we store file objects
        extra_metadata = {k: v for k, v in last_user_msg.items() if k not in ["role", "content", "api_payload", "uploaded_files_obj"]}
    else:
        prompt = user_input
        extra_metadata = {} # Reset for new input

    # CHECK LIMITS
    if not check_usage_limit(username):
        st.error("🚨 Daily Limit Reached! Please upgrade to Premium to continue.")
    else:
        # Process Message
        models_to_try = []
        api_content = prompt
        memory_content = prompt
        
        # If this is a new user input, we need to process files.
        # If it's a regeneration, files are already in extra_metadata (or we need to re-process if not stored)
        # For simplicity, let's assume for regeneration, we use the stored metadata.
        # For new input, we process `uploaded_files`.

        if uploaded_files:
             # Use Helper Function
             api_content, memory_content, models_to_try, extra_metadata = process_file_batch(prompt, uploaded_files)
        else:
            models_to_try = [MODEL_TEXT_MAIN, MODEL_TEXT_BACKUP]

        # Save User Message
        msg_obj = {"role": "user", "content": memory_content, "api_payload": api_content}
        msg_obj.update(extra_metadata)
        
        if is_regeneration:
             # Update the existing last message (Edit Mode)
             st.session_state.chat_history[active_id][-1] = msg_obj
        else:
             # Append new message (Normal Mode)
             st.session_state.chat_history[active_id].append(msg_obj)
        
        # Show User Message
        with st.chat_message("user"):
            if "file_names" in extra_metadata:
                for fname in extra_metadata["file_names"]:
                    st.info(f"📎 {fname}")
            if "display_images" in extra_metadata:
                for img in extra_metadata["display_images"]:
                    st.image(img, width=300)
            
            # Fallback for old history (pre-migration)
            if "display_file" in extra_metadata:
                st.info(f"📎 {extra_metadata['display_file']}")
            if "display_image" in extra_metadata:
                st.image(extra_metadata['display_image'], width=300)
                
            st.write(prompt)

        # Generate Answer
        with st.chat_message("assistant"):
            # Clean history for API
            clean_history = []
            # MEMORY MANAGEMENT: Only take last 10 messages to save tokens
            recent_history = st.session_state.chat_history[active_id][-10:]
            
            for m in recent_history:
                payload = m.get("api_payload", m["content"])
                # If image payload but not vision model, simplify
                # Vision model names: "vision", "maverick", "scout", "llama-4" (vision-capable models)
                is_vision_model = any(kw in models_to_try[0].lower() for kw in ["vision", "maverick", "scout", "llama-4"])
                if isinstance(payload, list) and not is_vision_model:
                     clean_history.append({"role": m["role"], "content": "[Image Content Sent]"})
                else:
                     clean_history.append({"role": m["role"], "content": payload})
            
            # STREAMING RESPONSE
            # Get custom instruction
            current_instruction = get_user_settings(username)
            
            stream_generator, used_model = generate_answer(clean_history, models_to_try, current_instruction)
            
            # Use st.write_stream if available (Streamlit 1.32+) or loop manually
            if used_model != "Error":
                answer = st.write_stream(stream_generator)
            else:
                answer = list(stream_generator)[0] # Error message
                st.write(answer)
                
            st.caption(f"⚡ {used_model}")
                
        # Increment Usage
        increment_usage(username)
        # Update UI immediately
        render_usage_bar(current_usage + 1, limit, subscription)
        
        # Save Assistant Message
        st.session_state.chat_history[active_id].append({
            "role": "assistant",
            "content": answer,
            "used_model": used_model
        })
        
        # Reset File Uploader for next message
        st.session_state["uploader_key"] += 1
        st.rerun()
