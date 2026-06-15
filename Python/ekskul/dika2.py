import re
from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

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

# Label masing-masing teks
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

print("Corpus setelah preprocessing:")
print(preprocessed_corpus)

# --- TF‑IDF Vectorization ---
print("\n--- TF‑IDF ---")
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_corpus)

print("Jumlah fitur (kata unik):", len(vectorizer.get_feature_names_out()))
print("Nama fitur (kata):")
print(vectorizer.get_feature_names_out())
print()

# --- Split data untuk training dan testing ---
X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix, labels, test_size=0.3, random_state=42
)

# --- Model SVM ---
print("--- Pelatihan Model SVM ---")
model = svm.SVC(kernel="linear")  # kernel linear cocok untuk teks
model.fit(X_train, y_train)
print("Model selesai dilatih.\n")

# --- Evaluasi pada data test ---
y_pred = model.predict(X_test)
print("--- Evaluasi Model ---")
print("Akurasi:", accuracy_score(y_test, y_pred))
print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred))

# --- Contoh prediksi teks baru ---
new_text = ["Polusi udara dari kendaraan semakin parah"]
# Preprocessing sama seperti sebelumnya
t_new = re.sub(r"[^a-zA-Z\s]", " ", new_text[0].lower()).split()
t_new = [stemmer.stem(w) for w in t_new if w not in STOPWORDS]
t_new_clean = " ".join(t_new)

# Konversi TF-IDF dan prediksi
new_vec = vectorizer.transform([t_new_clean])
prediction = model.predict(new_vec)

print("\n--- Prediksi Contoh ---")
print("Teks :", new_text[0])
print("Preprocessed:", t_new_clean)
print("Prediksi label:", prediction[0])