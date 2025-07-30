import tkinter as tk

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

send_button = tk.Button(input_frame, text="Send") 
send_button.pack(pady=(0, 10))

def get_bot_reply(message):
    if "hello" in message.lower():
        return "Hello there!"
    elif "how are you" in message.lower():
        return "I'm good, thank you!"
    elif "your name" in message.lower():
        return "I'm SMP Chatbot."
    else:
        return "Sorry, I don't understand that yet."

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

message_entry.bind("<Return>", send_message_event)
send_button.config(command=send_message)

root.mainloop()
