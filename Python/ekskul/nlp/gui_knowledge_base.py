import tkinter as tk
import re

KNOWLEDGE_BASE = {
    "what is taman rama": "Taman Rama is an international school in Bali that provides education from kindergarten to senior high school.",
    "curriculum taman rama": "Taman Rama combines the Indonesian National Curriculum with international programs such as Cambridge Assessment.",
    "facilities taman rama": "The school has libraries, science laboratories, sports fields, music rooms, and computer labs.",
    "extracurricular activities taman rama": "Students can join sports, music, art, dance, and debate clubs."
}

def preprocess_text(text):
    # convert to lowercase
    text = text.lower()
    # remove symbols/numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_response(user_input):
    processed = preprocess_text(user_input)
    if processed in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[processed]
    else:
        return "Sorry, I don't have information about that."

def send_message():
    message = message_entry.get()
    if message.strip() != "":
        chat_area.config(state="normal")  
        chat_area.insert(tk.END, "You: " + message + "\n")
        
        # Get bot's response
        bot_response = get_response(message)
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n")
        
        chat_area.config(state="disabled")  
        message_entry.delete(0, tk.END)
        
def send_message_event(event):
    send_message()

root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("500x400")
root.resizable(False, False)

chat_area = tk.Text(root, height=15, width=55, state="disabled")
chat_area.pack(pady=(20, 20))

input_frame = tk.Frame(root)
input_frame.pack(padx=(0, 10), pady=(0, 10))

message_entry = tk.Entry(input_frame, width=35)
message_entry.pack(side="left", padx=(10, 10), pady=(0, 10))
message_entry.bind("<Return>", send_message_event)

send_button = tk.Button(input_frame, text="Send") 
send_button.pack(side="right", padx=(0, 0), pady=(0, 10))
send_button.config(command=send_message)

root.mainloop()