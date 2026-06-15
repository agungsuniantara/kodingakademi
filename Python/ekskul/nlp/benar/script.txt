import tkinter as tk
from tkinter import ttk

def send_message():
    message = message_entry.get().strip()
    if message:
        chat_area.config(state="normal")
        chat_area.insert(tk.END, "You: " + message + "\n\n", "user")

        bot_response = "hello"
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")

        chat_area.config(state="disabled")
        chat_area.see(tk.END)
        message_entry.delete(0, tk.END)

def send_message_event(event):
    send_message()

root = tk.Tk()
root.title("Taman Rama Chatbot")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#211F24")

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Vertical.TScrollbar",
    background="#2F2C35",
    troughcolor="#211F24",
    bordercolor="#2F2C35",
    arrowcolor="white"
)

chat_frame = tk.Frame(root, bg="#211F24")
chat_frame.pack(padx=20, pady=20, fill="both", expand=True)

chat_area = tk.Text(
    chat_frame,
    height=20,
    width=60,
    state="disabled",
    bg="#2F2C35",
    fg="white",
    font=("Arial", 14),
    relief="flat",
    wrap="word"
)
chat_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(
    chat_frame,
    orient="vertical",
    command=chat_area.yview,
    style="Vertical.TScrollbar"
)
scrollbar.pack(side="right", fill="y")
chat_area.config(yscrollcommand=scrollbar.set)

chat_area.tag_config("user", foreground="#8DE0A7", font=("Arial", 14, "bold"))
chat_area.tag_config("bot", foreground="#BB86FC", font=("Arial", 14))

input_frame = tk.Frame(root, bg="#211F24")
input_frame.pack(padx=20, pady=(0, 20), fill="x")

message_entry = tk.Entry(
    input_frame,
    width=50,
    bg="#3C393F",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Arial", 15),
    highlightbackground="#555555",
    highlightthickness=1
)
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
message_entry.bind("<Return>", send_message_event)

send_button = tk.Button(
    input_frame,
    text="Send",
    bg="#9B59B6",
    fg="white",
    relief="flat",
    font=("Arial", 15, "bold"),
    padx=15,
    pady=8,
    command=send_message
)
send_button.pack(side="right")

root.mainloop()