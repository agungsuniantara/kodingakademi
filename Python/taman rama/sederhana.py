knowledge = {
    "makanan": "rendang adalah makanan favorit di indonesia",
    "minuman": "aqua adalah minuman favorit di indonesia",
    "sekolah": "sekolah favorit di indonesia adalah taman rama"
}

input_user = input("Saya: ")

if input_user in knowledge:
    print(f"Chatbot: {knowledge[input_user]}")
else:
    print("Chatbot: Maaf, saya belum tahu tentang itu.")