import re
from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Stopword sederhana
STOPWORDS = {
    "yang",
    "dan",
    "di",
    "ke",
    "dari",
    "untuk",
    "pada",
    "dengan",
    "adalah",
    "itu",
    "ini",
    "sebagai",
    "atau",
    "dalam",
    "karena",
    "bagi",
    "oleh",
    "juga",
    "agar",
    "sebuah",
    "apa",
    "saya",
    "anda",
}

# Contoh dataset (ulasan)
corpus = [
    "Harga tiket transportasi umum sangat terjangkau dan bersih.",
    "Kendaraan bermotor menghasilkan banyak asap hitam yang mencemari udara.",
    "Terminal bus baru sangat nyaman dan rapi.",
    "Asap kendaraan membuat pernapasan sulit, sangat tidak sehat.",
    "Pemerintah menyediakan jalur sepeda yang aman dan luas.",
    "Saya benci kemacetan, polusi dari motor sangat parah.",
]

# Label masing-masing teks (0 = wajar, 1 = tidak wajar)
labels = ["wajar", "tidak wajar", "wajar", "tidak wajar", "wajar", "tidak wajar"]

# --- Tahapan Preprocessing ---
print("--- Tahapan Preprocessing ---\n")

factory = StemmerFactory()
stemmer = factory.create_stemmer()

preprocessed_corpus = []

for text in corpus:
    print("Teks asli:", text)

    # 1️⃣ Case folding
    text = text.lower()

    # 2️⃣ Cleaning (hapus tanda baca dan angka)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # 3️⃣ Tokenisasi
    tokens = text.split()

    # 4️⃣ Stopword removal
    tokens = [t for t in tokens if t not in STOPWORDS]

    # 5️⃣ Stemming
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    # 6️⃣ Gabungkan kembali
    cleaned_text = " ".join(stemmed_tokens)
    preprocessed_corpus.append(cleaned_text)

    print("Hasil akhir preprocessing:", cleaned_text)
    print()
    
print(preprocessed_corpus)

# --- TF‑IDF Vectorization ---
print("\n--- Hasil TF‑IDF ---")

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_corpus)

print("Kata-kata (fitur):")
print(vectorizer.get_feature_names_out())
print("\nMatriks TF‑IDF:")
print(tfidf_matrix.toarray())

# --- Gabungkan dengan label ---
print("\n--- Data Akhir (TF‑IDF + Label) ---")
for i, text in enumerate(preprocessed_corpus):
    print(f"Teks {i+1}: {text}")
    print("Label :", labels[i])
    print()