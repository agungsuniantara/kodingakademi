import pandas as pd
import json

# Membaca data dari file Excel 
file_excel = pd.read_excel('chatbot\Dataset_Chatbot.xlsx', 
sheet_name='intents') 
 
# Mengisi nilai-nilai yang kosong pada kolom "tag" dengan nilai sebelumnya 
file_excel['tag'].fillna(method='ffill', inplace=True) 
 
# Grouping data berdasarkan kolom "tag" dan menggabungkan patterns dan responses menjadi list 
grouped_data = file_excel.groupby('tag').agg({ 
    'patterns': lambda x: x.tolist(), 
    'responses': lambda x: x.tolist(), 
    'context': 'first', 
    'kota': lambda x: x.tolist(), 
    'harga': lambda x: x.tolist() 
}).reset_index() 
 
# Menghilangkan elemen-elemen kosong dari daftar “patterns”,  "responses", "kota", dan "harga" 
grouped_data['patterns'] = grouped_data['patterns'].apply(lambda x: [i for i in x if pd.notna(i)] if isinstance(x, list) else []) 
grouped_data['responses'] = grouped_data['responses'].apply(lambda x: [i for i in x if 
pd.notna(i)] if isinstance(x, list) else []) 
grouped_data['kota'] = grouped_data['kota'].apply(lambda x: 
[i for i in x if pd.notna(i)] if isinstance(x, list) else []) 
grouped_data['harga'] = grouped_data['harga'].apply(lambda x: 
[int(i) for i in x if pd.notna(i)] if isinstance(x, list) 
else []) 

# Konversi menjadi JSON dengan format lebih terstruktur dan tambahkan judul intents 
json_data = json.loads(grouped_data.to_json(orient='records')) 
 
# Simpan data JSON ke dalam file terpisah 
with open('dataset.json', 'w') as file: 
    json.dump({"intents": json_data}, file, indent=2, 
separators=(',', ': ')) 
 
print('Dataset JSON berhasil tersimpan "dataset.json"')