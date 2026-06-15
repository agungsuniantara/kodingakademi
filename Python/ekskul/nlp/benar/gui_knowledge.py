import tkinter as tk
from tkinter import ttk  # Import ttk for themed widgets

# Basis pengetahuan chatbot
KNOWLEDGE_BASE = {
    "what is taman rama": "Taman Rama is an international school in Bali that provides education from kindergarten to senior high school.",
    "curriculum taman rama": "Taman Rama combines the Indonesian National Curriculum with international programs such as Cambridge Assessment.",
    "facilities taman rama": "The school has libraries, science laboratories, sports fields, music rooms, and computer labs.",
    "extracurricular activities taman rama": "Students can join sports, music, art, dance, and debate clubs."
}

# Fungsi untuk mendapatkan respons dari chatbot
def get_response(input_message):
    # Ubah input menjadi huruf kecil untuk pencocokan yang tidak sensitif huruf besar/kecil
    input_message = input_message.lower()
    if input_message in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[input_message]
    else:
        return "Sorry, I don't have information about that."

# Fungsi untuk mengirim pesan
def send_message():
    message = message_entry.get().strip() # Ambil pesan dan hapus spasi di awal/akhir
    if message: # Pastikan pesan tidak kosong
        chat_area.config(state="normal")  # Izinkan edit untuk menambahkan teks
        
        # Tampilkan pesan pengguna
        chat_area.insert(tk.END, "You: " + message + "\n", "user") # Tag "user" untuk styling
        
        # Dapatkan dan tampilkan respons bot
        bot_response = get_response(message)
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n", "bot") # Tag "bot" untuk styling
        
        chat_area.config(state="disabled")  # Nonaktifkan edit lagi
        chat_area.see(tk.END) # Scroll otomatis ke bawah
        message_entry.delete(0, tk.END) # Hapus teks dari input entry

# Fungsi yang dipanggil saat tombol Enter ditekan
def send_message_event(event):
    send_message()

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Taman Rama Chatbot")
root.geometry("600x600") # Ukuran jendela yang lebih besar
root.resizable(False, False) # Nonaktifkan resize
root.configure(bg="#211F24") # Latar belakang gelap utama

# --- Styling ---
# Menentukan gaya untuk Text widget agar pesan terlihat berbeda
root.tag_config("user", foreground="#8DE0A7", font=("Arial", 10, "bold")) # Hijau muda untuk pengguna
root.tag_config("bot", foreground="#BB86FC", font=("Arial", 10)) # Ungu muda untuk bot

# Gaya untuk Scrollbar (membutuhkan ttk)
style = ttk.Style()
style.theme_use('clam') # Menggunakan tema 'clam' sebagai dasar
style.configure("Vertical.TScrollbar",
                background="#2F2C35",
                troughcolor="#211F24",
                bordercolor="#2F2C35",
                arrowcolor="white")


# --- Chat Area ---
chat_frame = tk.Frame(root, bg="#211F24")
chat_frame.pack(padx=20, pady=20, fill="both", expand=True)

chat_area = tk.Text(
    chat_frame,
    height=20,
    width=60,
    state="disabled",
    bg="#2F2C35",  # Latar belakang area chat yang lebih gelap
    fg="white",  # Warna teks default
    font=("Arial", 10),
    relief="flat", # Tanpa border
    wrap="word" # Wrap teks per kata
)
chat_area.pack(side="left", fill="both", expand=True)

# Scrollbar untuk area chat
scrollbar = ttk.Scrollbar(
    chat_frame,
    orient="vertical",
    command=chat_area.yview,
    style="Vertical.TScrollbar"
)
scrollbar.pack(side="right", fill="y")
chat_area.config(yscrollcommand=scrollbar.set)


# --- Input Frame ---
input_frame = tk.Frame(root, bg="#211F24")
input_frame.pack(padx=20, pady=(0, 20), fill="x")

# Entry untuk pesan
message_entry = tk.Entry(
    input_frame,
    width=50,
    bg="#3C393F",  # Latar belakang input yang lebih gelap
    fg="white",
    insertbackground="white", # Warna kursor
    relief="flat",
    font=("Arial", 11),
    highlightbackground="#555555", # Sedikit border tipis
    highlightthickness=1,
)
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
message_entry.bind("<Return>", send_message_event) # Bind tombol Enter

# Tombol Send
send_button = tk.Button(
    input_frame,
    text="Send",
    bg="#9B59B6", # Warna ungu
    fg="white",
    relief="flat",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    command=send_message,
)
send_button.pack(side="right")

# Jalankan aplikasi
root.mainloop()