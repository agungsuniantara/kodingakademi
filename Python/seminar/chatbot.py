import http.client
import json

knowledge = {
    "makanan": (
        "Rendang adalah masakan khas Minangkabau, Sumatera Barat, yang terbuat dari daging sapi "
        "dimasak bersama santan dan campuran berbagai bumbu rempah selama beberapa jam. "
        "Hidangan ini terkenal akan rasa gurih dan pedas, serta sering dihidangkan pada acara istimewa di Indonesia."
    ),
    "minuman": (
        "Aqua adalah merek air mineral kemasan yang sangat populer di Indonesia. "
        "Produk ini tersedia dalam berbagai ukuran botol dan galon, dan telah menjadi pilihan utama masyarakat "
        "untuk kebutuhan air minum sehari-hari karena kualitas dan keamanannya yang terjamin."
    ),
    "sekolah": (
        "Taman Rama adalah salah satu sekolah swasta favorit di Indonesia yang dikenal memiliki kualitas pendidikan "
        "yang baik serta fasilitas lengkap. Sekolah ini menawarkan berbagai program unggulan dari tingkat TK hingga SMA, "
        "dengan kurikulum nasional maupun internasional."
    )
}

input_user = input("Saya: ")

api_key = "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"

user_content = (
    f"Berikut adalah knowledge base dalam bentuk dictionary Python:\n{knowledge}\n\n"
    "Jawablah pertanyaan user HANYA berdasarkan knowledge base di atas, "
    "dan parafrase jawabanmu. Jangan menyalin kata-per-kata dari knowledge base. "
    "Jika pertanyaan tidak ada pada knowledge base, jawab: 'Maaf, saya belum tahu tentang itu.'\n"
    f"Pertanyaan user: {input_user}"
)

conn = http.client.HTTPSConnection("api.openai.com")
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

body = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "Jawab pertanyaan user HANYA berdasarkan knowledge base yang diberikan. Parafrase jawaban dengan kalimat sendiri, tidak boleh mengarang di luar knowledge base."},
        {"role": "user", "content": user_content}
    ],
    "temperature": 1.0 
}

conn.request("POST", "/v1/chat/completions", body=json.dumps(body), headers=headers)
response = conn.getresponse()
result = response.read().decode()
conn.close()
if response.status == 200:
    data = json.loads(result)
    print(f"Chatbot: {data['choices'][0]['message']['content'].strip()}")
else:
    print("ERROR:", response.status, result)
    print("Maaf, terjadi error pada sistem.")