import requests

TOKEN_BOT = "TOKEN_BOT_TELEGRAM"

def telegram(chat_id, file_path, caption):
    url = f"https://api.telegram.org/bot{TOKEN_BOT}/sendPhoto"
    print("\n--- Mengirim Gambar ke Telegram ---")
    try:
        with open(file_path, 'rb') as photo:
            response = requests.post(
                url, 
                files={'photo': photo}, 
                data={'chat_id': chat_id, 'caption': caption, 'parse_mode': 'Markdown'}
            )
            if response.status_code == 200:
                print(f"[SUKSES] Gambar berhasil dikirim ke Telegram!")
            else:
                print(f"[GAGAL] Respon Telegram: {response.text}")
    except Exception as e:
        print(f"[ERROR] Gagal mengirim: {e}")