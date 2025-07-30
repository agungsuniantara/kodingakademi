import tkinter as tk

root = tk.Tk()

root.title("Simple Chatbot")      # Set the window title
root.geometry("400x300")          # Set the window size (width x height)
root.configure(bg="lightblue")

label1 = tk.Label(root, text="Welcome to the Simple Chatbot!")
label1.pack()

label2 = tk.Label(
    root,
    text="Welcome to the Simple Chatbot!",
    bg="lightblue",
    font=("Arial", 14, "bold")
)
label2.pack(pady=10)

root.mainloop()

