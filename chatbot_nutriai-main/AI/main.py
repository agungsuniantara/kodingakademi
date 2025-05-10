# chatbot_gui.py

import tkinter as tk
from tkinter import PhotoImage, Scrollbar
from meal_engine import generate_meal_plan, welcome_message
import time
from PIL import Image, ImageTk  # Only used to load the output image if needed

# Inisialisasi jendela utama
root = tk.Tk()
root.title("SmartMealPlanner ChatBot")
root.geometry("700x700")
root.configure(bg="black")

# Header
header = tk.Frame(root, bg="#222")
header.pack(fill=tk.X)
title = tk.Label(header, text="SmartMealPlanner ChatBot", bg="#222", fg="white", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Canvas dan scrollbar untuk area chat
canvas = tk.Canvas(root, bg="black", highlightthickness=0)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg="black")

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Tampilkan pesan awal
def display_message(sender, text, align="w"):
    time_label = tk.Label(frame, text=time.strftime("%H:%M"), font=("Arial", 8), fg="gray", bg="black")
    time_label.pack(anchor=align, padx=10)

    message_label = tk.Label(frame, text=text, wraplength=600, justify="left", font=("Arial", 12),
                             bg="#444" if sender == "bot" else "#28a745", fg="white", padx=10, pady=5)
    message_label.pack(anchor=align, padx=10, pady=5)

display_message("bot", welcome_message, align="w")

# Fungsi kirim pesan
def send_message():
    message = entry.get()
    if message.strip() == "":
        return

    display_message("user", message, align="e")
    entry.delete(0, tk.END)

    response = generate_meal_plan(message)
    display_message("bot", response, align="w")

    if "meal_plan_nutrition.png" in response:
        try:
            img = Image.open("meal_plan_nutrition.png")
            img = img.resize((600, 400))
            photo = ImageTk.PhotoImage(img)
            label_img = tk.Label(frame, image=photo, bg="black")
            label_img.image = photo
            label_img.pack(pady=10)
        except Exception as e:
            display_message("bot", f"(Gagal menampilkan grafik: {e})", align="w")

    root.after(100, lambda: canvas.yview_moveto(1.0))

# Frame input
input_frame = tk.Frame(root, bg="#111")
input_frame.pack(fill=tk.X, side="bottom")

entry = tk.Entry(input_frame, font=("Arial", 14))
entry.pack(side="left", fill=tk.X, expand=True, padx=10, pady=10)

send_btn = tk.Button(input_frame, text="Kirim", command=send_message, bg="#28a745", fg="white", font=("Arial", 12))
send_btn.pack(side="right", padx=10)

# Enter = kirim pesan
root.bind("<Return>", lambda event: send_message())

# Jalankan aplikasi
root.mainloop()
