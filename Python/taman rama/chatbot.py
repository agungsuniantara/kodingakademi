import http.client
import json

knowledge = {
    "makanan": "rendang adalah makanan favorit di indonesia",
    "minuman": "aqua adalah minuman favorit di indonesia",
    "sekolah": "sekolah favorit di indonesia adalah taman rama"
}

api_key = "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"

print("Chatbot aktif! Ketik 'exit' untuk keluar.")

while True:
    user_input = input("Anda: ").lower().strip()
    if user_input == "exit":
        print("Chatbot: Sampai jumpa!!!")
        break

    found = False
    for key in knowledge:
        if key in user_input:
            print(f"Chatbot: {knowledge[key]}")
            found = True
            break 

    if not found:
        print("Chatbot: Maaf, saya belum tahu tentang itu.")
