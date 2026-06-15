from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

# ==========================================
# 1. KONFIGURASI API GOOGLE SHEETS
# ==========================================
SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load kredensial Service Account
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPES)
client = gspread.authorize(creds)

# Nama File Spreadsheet dan Nama Tab/Sheet
SHEET_NAME = "Data Leads Target" 
TAB_NAME = "Leads"

# ==========================================
# 2. ENDPOINT API
# ==========================================
@app.route('/submit-lead', methods=['POST'])
def submit_lead():
    try:
        # Tangkap payload JSON dari Postman/Frontend
        data = request.get_json()
        
        if not data:
            return jsonify({"status": "error", "message": "Payload JSON kosong"}), 400

        # Buka dokumen Google Sheets
        sheet = client.open(SHEET_NAME).worksheet(TAB_NAME)
        
        # Ambil baris pertama (Row 1) sebagai acuan Header Kolom
        headers = sheet.row_values(1)
        
        if not headers:
            return jsonify({
                "status": "error", 
                "message": "Sheet kosong. Buat minimal 1 baris di paling atas untuk nama kolom (header)."
            }), 400

        # Siapkan list kosong sepanjang jumlah kolom header
        row_to_insert = [''] * len(headers)

        # ==========================================
        # 3. PEMETAAN DATA DINAMIS
        # ==========================================
        for index, header in enumerate(headers):
            # Normalisasi nama header (huruf kecil, hapus spasi berlebih)
            header_key = header.lower().strip()
            
            # Cek jika header adalah kolom waktu/tanggal
            if header_key in ['waktu', 'timestamp', 'tanggal']:
                # Format: YYYY-MM-DD HH:MM:SS
                row_to_insert[index] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Cek jika data dikirim melalui JSON
            elif header_key in data:
                row_to_insert[index] = data[header_key]
                
            # Beri nilai default untuk kolom 'sumber' jika tidak ada di JSON
            elif header_key == 'sumber':
                row_to_insert[index] = 'API Flask'

        # ==========================================
        # 4. EKSEKUSI PENYIMPANAN KE SHEETS
        # ==========================================
        # Gunakan parameter tambahan agar TIDAK OVERWRITE
        sheet.append_row(
            row_to_insert,
            value_input_option='USER_ENTERED', # Memastikan angka/tanggal formatnya benar di Sheet
            insert_data_option='INSERT_ROWS'   # Memaksa baris baru ditambahkan ke bawah
        )
        
        return jsonify({
            "status": "success", 
            "message": "Data berhasil dipetakan dan disimpan sebagai baris baru.",
            "inserted_data": row_to_insert
        }), 201

    # ==========================================
    # 5. PENANGANAN ERROR
    # ==========================================
    except gspread.exceptions.SpreadsheetNotFound:
        return jsonify({"status": "error", "message": f"Spreadsheet '{SHEET_NAME}' tidak ditemukan. Pastikan sudah di-share ke email Service Account."}), 404
    except gspread.exceptions.WorksheetNotFound:
        return jsonify({"status": "error", "message": f"Tab '{TAB_NAME}' tidak ditemukan."}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Jalankan server di port 5000
    app.run(debug=True, port=5000)