import customtkinter

def show_input():
    user_text = entry.get()
    print("User typed:", user_text)

app = customtkinter.CTk()
app.geometry("300x200")

# Input Field
entry = customtkinter.CTkEntry(app, placeholder_text="Type something...")
entry.pack(pady=20)

# Submit Button
btn = customtkinter.CTkButton(app, text="Submit", command=show_input)
btn.pack(pady=10)

app.mainloop()