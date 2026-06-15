import tkinter as tk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

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

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

def get_chatbot_response(user_input):
    input_emb = get_embeddings([user_input])
    similarities = cosine_similarity(input_emb, kb_embeddings)[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]
    threshold = 0.70
    if best_score >= threshold:
        return KNOWLEDGE_BASE[kb_keys[best_index]]
    else:
        return "Sorry, I don’t understand your question"

def send_message():
    message = message_entry.get()
    if message.strip() != "":
        chat_area.config(state="normal")  
        chat_area.insert(tk.END, "You: " + message + "\n")
        bot_response = get_chatbot_response(message)
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n")
        chat_area.config(state="disabled")  
        message_entry.delete(0, tk.END)
        
def send_message_event(event):
    send_message()
    
kb_keys = list(KNOWLEDGE_BASE.keys())
kb_embeddings = get_embeddings(kb_keys)

root = tk.Tk()
root.title("Chatbot")
root.geometry("500x400")
root.resizable(False, False)

chat_area = tk.Text(root, height=15, width=55, state="disabled")
chat_area.pack(pady=(20, 20))

input_frame = tk.Frame(root)
input_frame.pack(padx=(0, 10), pady=(0, 10))

message_entry = tk.Entry(input_frame, width=35)
message_entry.pack(side="left", padx=(10, 10), pady=(0, 10))
message_entry.bind("<Return>", send_message_event)

send_button = tk.Button(input_frame, text="Send", command=send_message) 
send_button.pack(side="right", padx=(0, 0), pady=(0, 10))

root.mainloop()
