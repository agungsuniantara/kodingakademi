import customtkinter as ctk
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch, re

# ===============   1. Tema Global  ===============
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ===============   2. Knowledge Base  ===============
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
  "apa itu EBT (Energi Baru Terbarukan)": "EBT adalah singkatan dari Energi Baru Terbarukan, yaitu sumber energi yang berasal dari proses alam yang berkelanjutan, seperti tenaga surya, angin, air (hidro), panas bumi, biomassa, dan ombak. Pengembangannya sangat penting untuk mengurangi emisi karbon.",
  "apa peran bank dalam mendukung pengurangan emisi karbon": "Bank dapat mendukung pengurangan emisi karbon dengan memberikan pinjaman untuk proyek energi terbarukan, mendanai inisiatif hijau, menawarkan produk keuangan berkelanjutan, dan mengadopsi kebijakan investasi yang bertanggung jawab lingkungan."
}

# ===============   3. Model Transformer Embedding  ===============
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask

def get_transformer_embeddings(texts):
    encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**encoded_input)
    sentence_embeddings = mean_pooling(model_output, encoded_input["attention_mask"])
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    return sentence_embeddings.cpu().numpy()

kb_keys = list(KNOWLEDGE_BASE.keys())
kb_embeddings = get_transformer_embeddings(kb_keys)

# ===============   4. Fungsi Chatbot   ===============
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def get_chatbot_response(user_input):
    processed_input = preprocess_text(user_input)
    if not processed_input:
        return "sorry, i dont understand"

    input_embedding = get_transformer_embeddings([processed_input])
    similarities = cosine_similarity(input_embedding, kb_embeddings)[0]
    best_match_index = similarities.argmax()
    max_similarity_score = similarities[best_match_index]
    if max_similarity_score >= 0.70:
        return KNOWLEDGE_BASE[kb_keys[best_match_index]]
    else:
        return "sorry, i dont understand"

# ===============   5. Kelas UI Chatbot   ===============
class CarbonChatbotApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # set fullscreen
        self.title("Carbon Chatbot (Fullscreen UI)")
        self.state("zoomed")  # fullscreen otomatis
        self.configure(fg_color="#0D0D0D")

        # grid utama
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # === Title ===
        self.title_label = ctk.CTkLabel(
            self,
            text="🌍 What can I help with?",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        )
        self.title_label.grid(row=0, column=0, pady=(40, 10), sticky="n")

        # === Chat Area ===
        self.chat_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="#1E1E1E",
            width=1000,
            height=500,
            border_width=0,
        )
        self.chat_frame.grid(row=1, column=0, sticky="nsew", padx=300, pady=10)

        # === Input section (sticky bottom) ===
        self.bottom_bar = ctk.CTkFrame(self, fg_color="#141414", height=90)
        self.bottom_bar.grid(row=2, column=0, sticky="ew", padx=0, pady=(10, 20))
        self.bottom_bar.grid_columnconfigure(0, weight=1)
        self.bottom_bar.grid_rowconfigure(0, weight=1)

        self.input_container = ctk.CTkFrame(self.bottom_bar, fg_color="#202020", corner_radius=50)
        self.input_container.grid(sticky="ew", padx=400, pady=10)
        self.input_container.grid_columnconfigure(0, weight=1)

        self.user_input = ctk.CTkEntry(
            self.input_container,
            placeholder_text="Ketik sesuatu...",
            height=50,
            font=("Segoe UI", 18),
            corner_radius=30,
            fg_color="#2A2A2A",
            border_width=0,
            text_color="white",
        )
        self.user_input.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="ew")
        self.user_input.bind("<Return>", self.send_message_event)
        self.user_input.bind("<KeyRelease>", self.update_suggestions)

        self.send_button = ctk.CTkButton(
            self.input_container,
            text="➤",
            width=60,
            height=40,
            fg_color="#2A2A2A",
            hover_color="#3C3C3C",
            font=("Segoe UI", 20),
            command=self.send_message,
            corner_radius=50,
        )
        self.send_button.grid(row=0, column=1, padx=10, pady=5)

        # === suggestion frame ===
        self.suggestion_frame = ctk.CTkFrame(self, fg_color="#0D0D0D")
        self.suggestion_frame.grid(row=3, column=0, sticky="ew", padx=420, pady=(0, 20))

        # pesan pembuka
        self.add_message("Chatbot", "Halo! ask anything about carbon emission 🌱")

    def add_message(self, sender, message):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="#1E1E1E")
        label = ctk.CTkLabel(
            frame,
            text=f"{sender}: {message}",
            anchor="w",
            justify="left",
            wraplength=800,
            font=("Segoe UI", 16),
            text_color="#eaeaea"
        )
        label.pack(fill="x", padx=10, pady=5)
        frame.pack(fill="x", padx=20, pady=5)

    def send_message_event(self, event=None):
        self.send_message()

    def send_message(self, text_from_suggestion=None):
        user_text = text_from_suggestion if text_from_suggestion else self.user_input.get()
        if user_text.strip() == "":
            return
        self.add_message("Anda", user_text)
        self.user_input.delete(0, "end")
        self.clear_suggestions()
        response = get_chatbot_response(user_text)
        self.add_message("Chatbot", response)

    def update_suggestions(self, event=None):
        typed = self.user_input.get().lower().strip()
        self.clear_suggestions()
        if not typed:
            return
        matches = [q for q in KNOWLEDGE_BASE.keys() if typed in q.lower()][:3]
        for s in matches:
            btn = ctk.CTkButton(
                self.suggestion_frame,
                text=s,
                command=lambda text=s: self.send_message(text),
                fg_color="#202020",
                hover_color="#303030",
                corner_radius=12,
                anchor="w",
                width=900,
                font=("Segoe UI", 14),
                text_color="#cccccc",
            )
            btn.pack(fill="x", pady=2)

    def clear_suggestions(self):
        for widget in self.suggestion_frame.winfo_children():
            widget.destroy()

# Jalankan aplikasi
if __name__ == "__main__":
    app = CarbonChatbotApp()
    app.mainloop()