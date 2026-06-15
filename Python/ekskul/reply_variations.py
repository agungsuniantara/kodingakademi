import tkinter as tk
import random

def get_bot_reply(message):
    msg = message.lower()
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon"]
    greet_replies = [
        "Hi there!",
        "Hello! How can I assist you?",
        "Hey! Glad to see you.",
        "Hi! What's up?"
    ]
    bye_keywords = ["bye", "goodbye", "see you"]
    bye_replies = [
        "Goodbye! See you next time.",
        "Bye! Take care.",
        "Hope to chat with you again soon."
    ]
    if any(greet in msg for greet in greetings):
        return random.choice(greet_replies)
    elif "how are you" in msg or "how do you do" in msg:
        return "I'm doing well, thank you for asking!"
    elif "weather" in msg:
        return "Sorry, I can't check the weather right now."
    elif "color" in msg or "favourite color" in msg or "favorite color" in msg:
        return "I like blue. What is your favorite color?"
    elif "joke" in msg:
        jokes = [
            "Why was the computer cold? It left its Windows open.",
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
        return random.choice(jokes)
    elif any(bye in msg for bye in bye_keywords):
        return random.choice(bye_replies)
    else:
        unknowns = [
            "Hmm, I don't understand that.",
            "Could you try asking in a different way?",
            "Sorry, I'm still learning new things."
        ]
        return random.choice(unknowns)

def send_message():
    message = message_entry.get()
    if message.strip() != "":
        chat_area.config(state="normal")
        chat_area.insert(tk.END, "You: " + message + "\n")
        bot_reply = get_bot_reply(message)
        chat_area.insert(tk.END, "Bot: " + bot_reply + "\n")
        chat_area.config(state="disabled")
        message_entry.delete(0, tk.END)

def send_message_event(event):
    send_message()

root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("500x400")
root.resizable(False, False)

chat_area = tk.Text(root, height=15, width=55, state="disabled")
chat_area.pack(pady=(10, 10))

input_frame = tk.Frame(root)
input_frame.pack(padx = (0, 10), pady=(0, 10))

message_entry = tk.Entry(input_frame, width=35)
message_entry.pack(side="left", padx=(10, 10), pady=(0, 10))
message_entry.bind("<Return>", send_message_event)

send_button = tk.Button(input_frame, text="Send") 
send_button.pack(pady=(0, 10))
send_button.config(command=send_message)

root.mainloop()
