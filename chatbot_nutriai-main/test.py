import http.client
import json

# Ganti dengan API key kamu
api_key = "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"  # Jangan hardcode di produksi

# Endpoint dan header
conn = http.client.HTTPSConnection("api.openai.com")
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Body request
body = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Apa itu machine learning?"}
    ],
    "temperature": 0.7
}

# Kirim request
conn.request("POST", "/v1/chat/completions", body=json.dumps(body), headers=headers)
response = conn.getresponse()

# Baca dan tampilkan hasil
data = response.read().decode()
hasil = json.loads(data)
print(hasil)
