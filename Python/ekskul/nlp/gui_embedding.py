import tkinter as tk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

KNOWLEDGE_BASE = {
    "what is taman rama": "Taman Rama is an international school in Bali that provides education from kindergarten to senior high school.",
    "curriculum taman rama": "Taman Rama combines the Indonesian National Curriculum with international programs such as Cambridge Assessment.",
    "facilities taman rama": "The school has libraries, science laboratories, sports fields, music rooms, and computer labs.",
    "extracurricular activities taman rama": "Students can join sports, music, art, dance, and debate clubs."
}

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

def get_chatbot_response(user_input):
    input_emb = get_embeddings([user_input])
    similarities = cosine_similarity(input_emb, kb_embeddings)[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]
    threshold = 0.65 
    if best_score >= threshold:
        return KNOWLEDGE_BASE[kb_keys[best_index]]
    else:
        return "Sorry, I don’t understand your question"

def send_message():
    message = message_entry.get()
    if message.strip() != "":
        chat_area.config(state="normal")  
        chat_area.insert(tk.END, "You: " + message + "\n")
        bot_response = get_chatbot_response(message)
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n")
        chat_area.config(state="disabled")  
        message_entry.delete(0, tk.END)
        
def send_message_event(event):
    send_message()
    
kb_keys = list(KNOWLEDGE_BASE.keys())
kb_embeddings = get_embeddings(kb_keys)

root = tk.Tk()
root.title("Chatbot")
root.geometry("500x400")
root.resizable(False, False)

chat_area = tk.Text(root, height=15, width=55, state="disabled")
chat_area.pack(pady=(20, 20))

input_frame = tk.Frame(root)
input_frame.pack(padx=(0, 10), pady=(0, 10))

message_entry = tk.Entry(input_frame, width=35)
message_entry.pack(side="left", padx=(10, 10), pady=(0, 10))
message_entry.bind("<Return>", send_message_event)

send_button = tk.Button(input_frame, text="Send", command=send_message) 
send_button.pack(side="right", padx=(0, 0), pady=(0, 10))

root.mainloop()