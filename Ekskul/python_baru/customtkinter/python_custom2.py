import customtkinter

def change_color(choice):
    print("Selected color:", choice)

app = customtkinter.CTk()
app.geometry("300x200")

label = customtkinter.CTkLabel(app, text="Choose a color:")
label.pack(pady=10)

# Dropdown Menu
colors = ["Red", "Green", "Blue", "Yellow"]
dropdown = customtkinter.CTkOptionMenu(app, values=colors, command=change_color)
dropdown.pack(pady=10)

# Setting a default value
dropdown.set("Green")

app.mainloop()