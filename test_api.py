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