import tkinter as tk
from tkinter import PhotoImage, Scrollbar
import time
import os
import random

# Fungsi respons chatbot
def generate_meal_plan(message):
    msg = message.lower()
    if "pagi" in msg:
        return "Menu sarapan sehat: Oatmeal, pisang, dan susu."
    elif "siang" in msg:
        return "Menu makan siang: Nasi merah, dada ayam, sayur rebus."
    elif "malam" in msg:
        return "Menu malam: Sup sayur dan tahu tempe."
    else:
        return "Silakan masukkan waktu makan (pagi, siang, malam)."

# Inisialisasi window
root = tk.Tk()
root.title("ChatBot Nutrisi")
root.geometry("500x600")
root.configure(bg="black")

# Header
header = tk.Frame(root, bg="#222")
header.pack(fill=tk.X)
title = tk.Label(header, text="ChatBot Nutrisi", bg="#222", fg="white", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Area chat dengan canvas scroll
canvas = tk.Canvas(root, bg="black")
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg="black")

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Tampilkan pesan selamat datang
def display_message(sender, text, align="w"):
    time_label = tk.Label(frame, text=time.strftime("%H:%M"), font=("Arial", 8), fg="gray", bg="black")
    time_label.pack(anchor=align, padx=10)

    message_label = tk.Label(frame, text=text, wraplength=300, justify="left", font=("Arial", 12),
                             bg="#444" if sender == "bot" else "#28a745", fg="white", padx=10, pady=5)
    message_label.pack(anchor=align, padx=10, pady=5)

display_message("bot", "Halo! Saya ChatBot Nutrisi.\nKetik waktu makanmu: pagi / siang / malam.", align="w")

# Fungsi kirim pesan
def send_message():
    message = entry.get()
    if message.strip() == "":
        return

    display_message("user", message, align="e")
    entry.delete(0, tk.END)

    response = generate_meal_plan(message)
    display_message("bot", response, align="w")

    # Scroll ke bawah
    root.after(100, lambda: canvas.yview_moveto(1.0))

# Input dan tombol kirim
input_frame = tk.Frame(root, bg="#111")
input_frame.pack(fill=tk.X, side="bottom")

entry = tk.Entry(input_frame, font=("Arial", 14))
entry.pack(side="left", fill=tk.X, expand=True, padx=10, pady=10)

send_btn = tk.Button(input_frame, text="Kirim", command=send_message, bg="#28a745", fg="white", font=("Arial", 12))
send_btn.pack(side="right", padx=10)

# Enter untuk kirim
root.bind("<Return>", lambda event: send_message())

# Jalankan aplikasi
root.mainloop()
