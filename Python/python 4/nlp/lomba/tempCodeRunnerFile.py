import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

# --- 1. Data Pengetahuan (Key-Value Pairs) ---
KNOWLEDGE_BASE = {
  "bagaimana kendaraan bermotor menyebabkan emisi karbon": "Kendaraan bermotor membakar bahan bakar fosil (bensin/diesel), melepaskan gas buang seperti karbon dioksida (CO2) dan gas rumah kaca lainnya yang berkontribusi pada pemanasan global.",
  "berapa kontribusi sektor transportasi terhadap emisi nasional": "Di Indonesia, sektor transportasi merupakan salah satu penyumbang emisi karbon terbesar. Menurut data, kontribusinya bisa mencapai sekitar 20-25% dari total emisi nasional, terutama dari penggunaan kendaraan pribadi.",
  "bagaimana cara mengurangi jejak karbon perjalanan saya": "Untuk mengurangi jejak karbon perjalanan Anda, pertimbangkan untuk beralih ke transportasi umum (bus, kereta), bersepeda, berjalan kaki, atau menggunakan kendaraan listrik/hybrid jika memungkinkan. Menggabungkan perjalanan dan mengemudi secara efisien juga membantu.",
  "apa dampak jika saya beralih dari motor ke transportasi publik selama setahun": "Jika Anda beralih dari motor ke transportasi publik selama setahun, Anda dapat mengurangi emisi CO2 secara signifikan, menghemat biaya bahan bakar, mengurangi kemacetan, dan berkontribusi pada udara yang lebih bersih. Estimasi pengurangan emisi bisa mencapai ratusan kilogram CO2 per tahun, tergantung jarak tempuh.",
  "apa itu emisi karbon": "Emisi karbon adalah pelepasan gas karbon ke atmosfer bumi, terutama karbon dioksida (CO2), yang sebagian besar dihasilkan dari pembakaran bahan bakar fosil oleh aktivitas manusia dan menjadi penyebab utama perubahan iklim.",
  "dampak emisi karbon bagi lingkungan": "Dampak emisi karbon antara lain pemanasan global, perubahan iklim ekstrem (banjir, kekeringan), kenaikan permukaan air laut, kerusakan ekosistem laut (pemutihan karang), dan masalah kesehatan akibat polusi udara.",
  "tips transportasi berkelanjutan": "Tips transportasi berkelanjutan meliputi: gunakan angkutan umum, bersepeda atau berjalan kaki untuk jarak dekat, pertimbangkan kendaraan listrik, manfaatkan carpooling, dan rawat kendaraan Anda agar efisien bahan bakar.",
  "definisi perubahan iklim": "Perubahan iklim adalah pergeseran signifikan dan jangka panjang dalam pola cuaca global atau regional, terutama disebabkan oleh peningkatan konsentrasi gas rumah kaca di atmosfer akibat aktivitas manusia.",
  "apa sumber utama emisi karbon": "Sumber utama emisi karbon meliputi pembakaran bahan bakar fosil untuk energi listrik dan transportasi, deforestasi, aktivitas industri, dan pertanian intensif yang menghasilkan gas metana (CH4) dan dinitrogen oksida (N2O).",
  "apa hubungan deforestasi dengan emisi karbon": "Deforestasi mengurangi kemampuan bumi menyerap karbon dioksida karena berkurangnya pepohonan. Selain itu, proses penebangan dan pembakaran hutan melepaskan karbon yang tersimpan di biomassa pohon ke atmosfer.",
  "bagaimana energi terbarukan dapat mengurangi emisi karbon": "Energi terbarukan seperti tenaga surya, angin, hidro, dan biomassa menghasilkan listrik tanpa membakar bahan bakar fosil. Dengan menggantikan sumber energi berbasis fosil, emisi CO2 dapat dikurangi secara drastis.",
  "apa dampak emisi karbon terhadap kesehatan manusia": "Emisi karbon sering kali disertai polutan lain seperti partikulat (PM2.5) dan nitrogen oksida yang dapat menyebabkan gangguan pernapasan, penyakit jantung, dan memperburuk kondisi kronis seperti asma.",
  "apa itu jejak karbon": "Jejak karbon adalah total emisi gas rumah kaca yang dihasilkan langsung maupun tidak langsung oleh aktivitas individu, organisasi, atau produk, biasanya dinyatakan dalam satuan kilogram atau ton CO2 ekuivalen.",
  "bagaimana cara menghitung jejak karbon pribadi": "Jejak karbon pribadi dihitung dari aktivitas sehari-hari seperti penggunaan kendaraan, konsumsi listrik, pola makan, dan perjalanan udara. Banyak kalkulator daring yang bisa memperkirakan emisi total berdasarkan data kegiatan Anda.",
  "apa itu netral karbon": "Netral karbon (carbon neutrality) berarti kondisi ketika jumlah emisi karbon yang dikeluarkan setara dengan jumlah yang diserap kembali melalui upaya seperti reboisasi, efisiensi energi, atau kompensasi karbon.",
  "contoh kebijakan pengurangan emisi karbon": "Beberapa kebijakan yang diterapkan negara untuk mengurangi emisi karbon antara lain penerapan pajak karbon, perdagangan emisi (carbon trading), subsidi energi terbarukan, dan larangan pembakaran hutan.",
  "apa peran individu dalam mitigasi emisi karbon": "Individu dapat berperan penting dengan mengadopsi gaya hidup berkelanjutan seperti menghemat energi, memilih transportasi ramah lingkungan, mengurangi konsumsi daging, dan mendukung produk atau perusahaan yang ramah lingkungan.",
  "perbedaan CO2 dan gas rumah kaca lainnya": "CO2 adalah gas rumah kaca paling umum dari pembakaran bahan bakar. Namun ada juga gas lain seperti metana (CH4), dinitrogen oksida (N2O), dan gas fluorinated yang memiliki efek pemanasan lebih besar meski dalam jumlah lebih sedikit.",
  "bagaimana sektor industri menyumbang emisi karbon": "Sektor industri menghasilkan emisi karbon melalui proses produksi, penggunaan energi fosil untuk mesin, dan reaksi kimia (seperti pembuatan semen dan baja) yang melepaskan CO2 ke atmosfer.",
  "apa hubungan konsumsi energi listrik dengan emisi karbon": "Sebagian besar listrik di Indonesia masih dihasilkan dari pembangkit berbahan batu bara atau gas. Semakin tinggi konsumsi listrik, semakin besar pula emisi karbon jika energi tersebut belum berasal dari sumber terbarukan.",
  "apa itu penyerapan karbon (carbon capture)": "Penyerapan karbon (Carbon Capture, Utilization, and Storage/CCUS) adalah teknologi yang menangkap CO2 dari sumber emisi besar (pembangkit listrik, pabrik), kemudian disimpan secara permanen di bawah tanah atau digunakan untuk tujuan lain.",
  "bagaimana pertanian dapat berkontribusi pada emisi karbon": "Pertanian dapat menyumbang emisi melalui penggunaan pupuk nitrogen (menghasilkan N2O), pencernaan ternak (menghasilkan metana dari sapi), dan perubahan penggunaan lahan seperti pembukaan lahan gambut.",
  "bagaimana kota-kota dapat mengurangi emisi karbon": "Kota-kota dapat mengurangi emisi dengan mempromosikan transportasi publik, mengembangkan infrastruktur hijau, meningkatkan efisiensi energi bangunan, mengelola limbah dengan baik, dan menggunakan sumber energi terbarukan.",
  "apa itu kredit karbon": "Kredit karbon adalah izin yang memungkinkan pemegang untuk mengeluarkan satu ton karbon dioksida. Ini dapat diperdagangkan, memungkinkan perusahaan untuk membeli 'hak' untuk beremisi atau menjual 'penghematan' emisi mereka.",
  "apa hubungan antara konsumsi daging dan emisi karbon": "Produksi daging, terutama daging merah, membutuhkan lahan, air, dan pakan yang besar. Ternak juga menghasilkan metana. Konsumsi daging yang lebih rendah dapat mengurangi jejak karbon pribadi secara signifikan.",
  "bagaimana teknologi cerdas dapat membantu mengurangi emisi": "Teknologi cerdas seperti smart grid, sensor IoT untuk efisiensi energi di bangunan, optimasi rute transportasi, dan analisis data untuk memprediksi konsumsi energi dapat membantu mengurangi emisi.",
  "apa itu transisi energi": "Transisi energi adalah pergeseran global dari sistem energi berbasis bahan bakar fosil ke sistem energi berkelanjutan yang mengandalkan sumber energi terbarukan dan teknologi rendah karbon.",
  "dampak emisi karbon pada biota laut": "Peningkatan CO2 di atmosfer menyebabkan lautan menyerap lebih banyak CO2, yang mengakibatkan pengasaman laut. Ini merusak kerang-kerangan, terumbu karang, dan ekosistem laut lainnya.",
  "apa itu karbon biru (blue carbon)": "Karbon biru adalah karbon yang disimpan di ekosistem pesisir dan laut seperti hutan bakau, padang lamun, dan rawa payau. Ekosistem ini sangat efektif dalam menyerap dan menyimpan karbon.",
  "bagaimana reboisasi dan aforestasi mengurangi emisi": "Reboisasi (penanaman kembali hutan) dan aforestasi (penanaman hutan di lahan yang belum pernah berhutan) membantu menyerap CO2 dari atmosfer melalui fotosintesis, menyimpannya di biomassa pohon dan tanah.",
  "apa itu mitigasi perubahan iklim": "Mitigasi perubahan iklim adalah tindakan untuk mengurangi emisi gas rumah kaca atau meningkatkan penyerapan gas rumah kaca, untuk memperlambat atau menghentikan pemanasan global.",
  "bagaimana pembangunan berkelanjutan berkaitan dengan emisi karbon": "Pembangunan berkelanjutan berupaya memenuhi kebutuhan generasi sekarang tanpa mengorbankan kemampuan generasi mendatang. Ini mencakup pengurangan emisi karbon melalui praktik ekonomi dan sosial yang bertanggung jawab lingkungan.",
  "apa itu EBT": "EBT adalah singkatan dari Energi Baru Terbarukan, yaitu sumber energi yang berasal dari proses alam yang berkelanjutan, seperti tenaga surya, angin, air (hidro), panas bumi, biomassa, dan ombak. Pengembangannya sangat penting untuk mengurangi emisi karbon.",
  "apa peran bank dalam mendukung pengurangan emisi karbon": "Bank dapat mendukung pengurangan emisi karbon dengan memberikan pinjaman untuk proyek energi terbarukan, mendanai inisiatif hijau, menawarkan produk keuangan berkelanjutan, dan mengadopsi kebijakan investasi yang bertanggung jawab lingkungan."
  "disini paragraf bukan key dan value"
}

# --- 2. Inisialisasi Model Transformer untuk Embedding ---

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def get_transformer_embeddings(texts):
    """
    Menghasilkan embedding (vektor representasi) untuk daftar teks menggunakan model Transformer.
    """
    # Tokenisasi input
    encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
    
    # Nonaktifkan perhitungan gradien untuk inferensi
    with torch.no_grad():
        model_output = model(**encoded_input)
    
    # Ambil embedding dari output [CLS] token dan lakukan mean pooling
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    
    # Normalisasi embedding
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    
    return sentence_embeddings.cpu().numpy()

# Fungsi mean pooling untuk menggabungkan token embeddings menjadi sentence embedding
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask

# Pra-hitung embedding untuk semua kunci dalam Knowledge Base
# Ini dilakukan sekali di awal untuk efisiensi
kb_keys = list(KNOWLEDGE_BASE.keys())
kb_embeddings = get_transformer_embeddings(kb_keys)

# --- 3. Fungsi Preprocessing Teks ---
def preprocess_text(text):
    """
    Melakukan preprocessing dasar pada teks: lowercase, hapus angka dan simbol.
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text) # Hapus selain huruf dan spasi
    text = re.sub(r'\s+', ' ', text).strip() # Ganti multiple spaces dengan single space
    return text

# --- 4. Fungsi Utama Chatbot Logic ---
def get_chatbot_response(user_input):
    """
    Menerima input pengguna, memprosesnya, dan mengembalikan jawaban terbaik.
    """
    processed_input = preprocess_text(user_input)

    if not processed_input:
        return "Maaf, saya tidak bisa memproses input kosong. Bisakah Anda bertanya lagi?"

    # Dapatkan embedding untuk input pengguna
    input_embedding = get_transformer_embeddings([processed_input])

    # Hitung cosine similarity antara input pengguna dan semua kunci di knowledge base
    similarities = cosine_similarity(input_embedding, kb_embeddings)[0]

    # Temukan indeks kunci dengan similarity tertinggi
    best_match_index = similarities.argmax()
    max_similarity_score = similarities[best_match_index]

    # Ambang batas similarity untuk memberikan jawaban
    # Anda bisa menyesuaikan nilai ini. Jika terlalu tinggi, chatbot bisa kurang responsif.
    # Jika terlalu rendah, chatbot bisa memberikan jawaban yang salah.
    similarity_threshold = 0.75

    if max_similarity_score >= similarity_threshold:
        best_match_key = kb_keys[best_match_index]
        response = KNOWLEDGE_BASE[best_match_key]
        return response
    else:
        return "Maaf, saya tidak memahami pertanyaan Anda. Bisakah Anda bertanya dengan cara lain atau mengenai topik emisi karbon dari transportasi?"

# --- 5. Antarmuka Pengguna Tkinter ---
class CarbonChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot Edukasi Emisi Karbon")
        master.geometry("1000x700")

        # Frame Chat
        self.chat_frame = tk.Frame(master)
        self.chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.chat_history = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            state='disabled',
            font=('Arial', 20)
        )
        self.chat_history.pack(fill=tk.BOTH, expand=True)

        # Frame Input
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=5, padx=10, fill=tk.X)

        self.user_input = tk.Entry(self.input_frame, width=60, font=('Arial', 20))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message_event)
        self.user_input.bind("<KeyRelease>", self.update_suggestions)  # << Tambah event ini

        self.send_button = tk.Button(
            self.input_frame, text="Kirim", command=self.send_message, font=('Arial', 15)
        )
        self.send_button.pack(side=tk.RIGHT)

        # Frame Rekomendasi (di bawah input)
        self.suggestion_frame = tk.Frame(master)
        self.suggestion_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

        # Pesan pembuka
        self.display_message(
            "Chatbot: Halo! Saya adalah Chatbot Edukasi Emisi Karbon. "
            "Tanyakan sesuatu tentang dampak transportasi terhadap emisi karbon di Indonesia.",
            "chatbot"
        )

    def display_message(self, message, sender):
        self.chat_history.config(state='normal')
        if sender == "user":
            self.chat_history.insert(tk.END, "Anda: " + message + "\n")
        else:
            self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview(tk.END)

    def send_message_event(self, event=None):
        self.send_message()

    def send_message(self, text_from_suggestion=None):
        """
        Mengirim pesan dari user (baik diketik langsung maupun dari tombol rekomendasi)
        """
        user_text = text_from_suggestion if text_from_suggestion else self.user_input.get()

        if user_text.strip() == "":
            return

        self.display_message(user_text, "user")
        self.user_input.delete(0, tk.END)
        self.clear_suggestions()  # Hapus tombol rekomendasi saat pesan dikirim

        chatbot_response = get_chatbot_response(user_text)
        self.display_message("Chatbot: " + chatbot_response, "chatbot")

    def update_suggestions(self, event=None):
        """
        Update tombol rekomendasi setiap kali user mengetik
        """
        typed = self.user_input.get().lower().strip()
        self.clear_suggestions()

        if not typed:
            return

        # Cari pertanyaan di knowledge base yang cocok sebagian
        matches = [
            q for q in KNOWLEDGE_BASE.keys()
            if typed in q.lower()
        ][:3]  # batas maksimal 3 rekomendasi

        for suggestion in matches:
            btn = tk.Button(
                self.suggestion_frame,
                text=suggestion,
                font=('Arial', 12),
                wraplength=700,
                anchor='w',
                justify='left',
                command=lambda s=suggestion: self.send_message(s)
            )
            btn.pack(fill=tk.X, pady=2)

    def clear_suggestions(self):
        """Hapus semua tombol rekomendasi."""
        for widget in self.suggestion_frame.winfo_children():
            widget.destroy()

# --- Jalankan Aplikasi ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CarbonChatbotApp(root)
    root.mainloop()