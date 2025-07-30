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
message_entry.pack(side = "left", padx=(10, 10), pady=(0, 10))

send_button = tk.Button(input_frame, text="Send") 
send_button.pack(side="right", padx=(0, 0), pady=(0, 10))

def send_message():
    message = message_entry.get()
    if message.strip() != "":
        chat_area.config(state="normal")  # Enable editing
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.config(state="disabled")  # Make read-only again
        message_entry.delete(0, tk.END)    # Clear input
        
def send_message_event(event):
    send_message()

message_entry.bind("<Return>", send_message_event)
send_button.config(command=send_message)

root.mainloop()
