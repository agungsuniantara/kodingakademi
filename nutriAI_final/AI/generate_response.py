import numpy as np
import re
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import http.client
import json
import os
import time
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.image import MIMEImage

def kirim_email_ke_pengguna(email_penerima, subject, isi_teks, path_gambar=None):
    """
    Fungsi email dengan debugging yang lebih detail
    """
    EMAIL_PENGIRIM = "theodarmawan0@gmail.com"
    PASSWORD = "urjn gkpl bqwa oajz"  # Ganti dengan App Password
    
    # Gunakan safe_print untuk menghindari error Unicode
    def safe_print(message):
        try:
            print(message)
        except UnicodeEncodeError:
            # Fallback ke ASCII dengan penggantian karakter
            print(message.encode('ascii', 'replace').decode('ascii'))
    
    safe_print(f"Mencoba mengirim email ke: {email_penerima}")
    safe_print(f"Dari: {EMAIL_PENGIRIM}")
    
    try:
        # Test koneksi terlebih dahulu
        safe_print("Testing koneksi ke Gmail...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as test_smtp:
            test_smtp.login(EMAIL_PENGIRIM, PASSWORD)
            safe_print("✓ Koneksi dan login berhasil")
        
        # Buat dan kirim email
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_PENGIRIM
        msg["To"] = email_penerima
        
        # Set konten HTML
        html_content = f"""
        <html>
        <body>
            <h2>📅 Rencana Makan 7 Hari Anda</h2>
            <div style="font-family: Arial, sans-serif; font-size: 14px; white-space: pre-wrap;">
                {isi_teks}
            </div>
        </body>
        </html>
        """
        
        msg.set_content("Silakan buka email ini dalam tampilan HTML.")
        msg.add_alternative(html_content, subtype='html')
        
        # Tambahkan gambar sebagai attachment
        if path_gambar and os.path.exists(path_gambar):
            try:
                with open(path_gambar, 'rb') as img_file:
                    img_data = img_file.read()
                    msg.add_attachment(img_data, 
                                     maintype='image', 
                                     subtype='png', 
                                     filename='grafik_nutrisi.png')
                safe_print("✓ Gambar berhasil ditambahkan")
            except Exception as img_error:
                safe_print(f"⚠ Gagal menambahkan gambar: {img_error}")
        
        # Kirim email
        safe_print("Mengirim email...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_PENGIRIM, PASSWORD)
            smtp.send_message(msg)
        
        safe_print("✓ Email berhasil dikirim!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        safe_print("❌ Gagal autentikasi Gmail")
        safe_print("Solusi:")
        safe_print("1. Pastikan 2FA diaktifkan di akun Gmail")
        safe_print("2. Buat App Password di Google Account Settings")
        safe_print("3. Gunakan App Password (16 karakter) bukan password biasa")
        return False
        
    except smtplib.SMTPRecipientsRefused:
        safe_print("❌ Email penerima ditolak")
        safe_print("Periksa format email penerima")
        return False
        
    except smtplib.SMTPServerDisconnected:
        safe_print("❌ Koneksi ke server terputus")
        safe_print("Coba lagi dalam beberapa saat")
        return False
        
    except Exception as e:
        safe_print(f"❌ Error tidak terduga: {e}")
        safe_print(f"Tipe error: {type(e).__name__}")
        return False

def dapatkan_resep_dari_api(persyaratan):
    api_key = os.environ.get("OPENAI_API_KEY", "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")
    conn = http.client.HTTPSConnection("api.openai.com")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    jenis_makan = persyaratan.get("jenis_makan", "makanan apa saja")
    kalori = persyaratan.get("kalori", "")
    protein = persyaratan.get("protein", "")
    karbohidrat = persyaratan.get("karbohidrat", "")
    lemak = persyaratan.get("lemak", "")
    pembatasan = ", ".join(persyaratan.get("pembatasan", []))
    alergi = ", ".join(persyaratan.get("alergi", []))
    
    prompt = f"""Buatkan satu resep {jenis_makan} sehat dengan kriteria berikut:
    - Target kalori: sekitar {kalori} kalori
    - Target makro: sekitar {protein}g protein, {karbohidrat}g karbohidrat, {lemak}g lemak
    """
    
    if pembatasan:
        prompt += f"- Pembatasan makanan: {pembatasan}\n"
    if alergi:
        prompt += f"- Harus menghindari (alergi): {alergi}\n"
    
    prompt += """Format respons Anda sebagai objek JSON dengan struktur berikut:
    {
      "nama": "Nama Resep",
      "kalori": 350,
      "protein": 20,
      "karbohidrat": 40,
      "lemak": 10,
      "bahan": "Daftar bahan dengan jumlah",
      "resep": "Petunjuk memasak langkah demi langkah"
    }
    
    Respons harus berupa JSON yang valid. Hanya sertakan objek JSON dalam respons Anda, tidak ada yang lain.
    """
    
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Anda adalah ahli gizi profesional dan koki yang mengkhususkan diri dalam perencanaan makanan sehat."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens":1500,
        "temperature": 0.7
    }
    
    try:
        conn.request("POST", "/v1/chat/completions", body=json.dumps(body), headers=headers)
        response = conn.getresponse()
        
        data = response.read().decode()
        hasil = json.loads(data)
        
        resep_json_str = hasil["choices"][0]["message"]["content"].strip()

        resep_json_str = re.sub(r'^```json\s*|\s*```$', '', resep_json_str, flags=re.MULTILINE)
        
        resep = json.loads(resep_json_str)
        return resep
        
    except Exception as e:
        print(f"Kesalahan dalam permintaan API: {e}")
        return {
            "nama": f"Cadangan {jenis_makan.capitalize()}",
            "kalori": persyaratan.get("kalori", 350),
            "protein": persyaratan.get("protein", 20),
            "karbohidrat": persyaratan.get("karbohidrat", 40),
            "lemak": persyaratan.get("lemak", 10),
            "bahan": "Silakan periksa koneksi API. Menggunakan resep cadangan.",
            "resep": "Kesalahan koneksi API. Ini adalah resep placeholder."
        }

cache_resep = {}

def dapatkan_atau_hasilkan_resep(jenis_makan, target, info_pengguna):
    kunci_pembatasan = "-".join(sorted(info_pengguna.get("pembatasan", [])))
    kunci_alergi = "-".join(sorted(info_pengguna.get("alergi", [])))
    kunci_cache = f"{jenis_makan}-{target['kalori']}-{kunci_pembatasan}-{kunci_alergi}"
    
    if kunci_cache in cache_resep:
        resep_list = cache_resep[kunci_cache]
        if resep_list:
            resep = resep_list.pop(0)
            resep_list.append(resep)
            return resep, format_resep(resep) #diuabah menjadi 2 nilai
    
    persyaratan = {
        "jenis_makan": jenis_makan,
        "kalori": target["kalori"],
        "protein": target["protein"],
        "karbohidrat": target["karbohidrat"],
        "lemak": target["lemak"],
        "pembatasan": info_pengguna.get("pembatasan", []),
        "alergi": info_pengguna.get("alergi", [])
    }
    
    resep = dapatkan_resep_dari_api(persyaratan)
    
    if kunci_cache not in cache_resep:
        cache_resep[kunci_cache] = []
    cache_resep[kunci_cache].append(resep)
    
    return resep, format_resep(resep) #diuabah menjadi 2 nilai

def format_resep(resep):
    formatted = f"""
🍽️ **{resep['nama']}**
----------------------------------------
🔥 **Nutrisi per porsi:**
- Kalori: **{resep['kalori']} kcal**
- Protein: **{resep['protein']}g**
- Karbohidrat: **{resep['karbohidrat']}g**
- Lemak: **{resep['lemak']}g**

🧂 **Bahan-bahan:**
{format_bahan(resep['bahan'])}

📝 **Langkah-langkah memasak:**
{format_langkah(resep['resep'])}
----------------------------------------
✨ _Selamat memasak dan tetap sehat!_
"""
    return formatted.strip()


def format_bahan(bahan_str):
    # Memecah jadi list dan beri emoji
    lines = bahan_str.strip().split('\n')
    return '\n'.join([f"✅ {line}" for line in lines if line.strip()])


def format_langkah(langkah_str):
    # Memecah jadi langkah-langkah bernomor
    lines = langkah_str.strip().split('\n')
    return '\n'.join([f"{line.strip()}_" for idx, line in enumerate(lines) if line.strip()])


pesan_selamat_datang = """
🍽️ Selamat Datang di NutriAI! 🍽️

Saya akan membantu Anda membuat rencana makan 7 hari yang dipersonalisasi berdasarkan kebutuhan kalori dan preferensi makronutrien Anda.

Untuk memulai, saya perlu mengumpulkan beberapa informasi:
1. Target kalori harian Anda
2. Preferensi makronutrien Anda (persentase protein/karbohidrat/lemak)
3. Pembatasan diet atau alergi

Siap untuk memulai? Ketik 'MULAI' untuk melanjutkan atau 'BANTUAN' untuk informasi lebih lanjut.
"""

pesan_bantuan = """
📋 Bantuan NutriAI 📋

Berikut adalah perintah yang dapat Anda gunakan:
- MULAI: Mulai proses perencanaan makan
- BANTUAN: Tampilkan pesan bantuan ini
- RESET: Mulai ulang dengan informasi baru
- KELUAR: Akhiri percakapan

Selama proses perencanaan makan, saya akan menanyakan tentang:
- Target kalori harian Anda (misalnya, 2000)
- Pembagian makronutrien (misalnya, 30% protein, 40% karbohidrat, 30% lemak)
- Pembatasan diet (misalnya, vegetarian, bebas gluten)
- Alergi makanan (misalnya, kacang, susu)

Setelah mengumpulkan informasi ini, saya akan menghasilkan rencana makan 7 hari yang dipersonalisasi dengan resep dan informasi gizi.
Setiap resep dibuat khusus berdasarkan persyaratan Anda menggunakan AI.

Siap untuk memulai? Ketik 'MULAI' untuk melanjutkan.
"""

info_pengguna = {
    "status": "awal",
    "kalori": 0,
    "persen_protein": 0,
    "persen_karbohidrat": 0,
    "persen_lemak": 0,
    "pembatasan": [],
    "alergi": []
}

def buat_rencana_makan(info_pengguna):
    rencana_makan = {}
    hari_ini = datetime.now()
    
    kalori_protein = info_pengguna["kalori"] * (info_pengguna["persen_protein"] / 100)
    kalori_karbohidrat = info_pengguna["kalori"] * (info_pengguna["persen_karbohidrat"] / 100)
    kalori_lemak = info_pengguna["kalori"] * (info_pengguna["persen_lemak"] / 100)
    
    gram_protein = kalori_protein / 4
    gram_karbohidrat = kalori_karbohidrat / 4
    gram_lemak = kalori_lemak / 9
    
    target_harian = {
        "kalori": info_pengguna["kalori"],
        "protein": gram_protein,
        "karbohidrat": gram_karbohidrat,
        "lemak": gram_lemak
    }
    
    distribusi_makan = {
        "sarapan": 0.25,
        "makan_siang": 0.35,
        "makan_malam": 0.40
    }
    
    for i in range(7):
        hari = (hari_ini + timedelta(days=i+1)).strftime("%A, %d %B")
        
        hari = hari.replace("Monday", "Senin").replace("Tuesday", "Selasa").replace("Wednesday", "Rabu")
        hari = hari.replace("Thursday", "Kamis").replace("Friday", "Jumat").replace("Saturday", "Sabtu")
        hari = hari.replace("Sunday", "Minggu")
        
        hari = hari.replace("January", "Januari").replace("February", "Februari").replace("March", "Maret")
        hari = hari.replace("April", "April").replace("May", "Mei").replace("June", "Juni")
        hari = hari.replace("July", "Juli").replace("August", "Agustus").replace("September", "September")
        hari = hari.replace("October", "Oktober").replace("November", "November").replace("December", "Desember")
        
        target_makan = {}
        for jenis_makan, persentase in distribusi_makan.items():
            target_makan[jenis_makan] = {
                "kalori": int(target_harian["kalori"] * persentase),
                "protein": int(target_harian["protein"] * persentase),
                "karbohidrat": int(target_harian["karbohidrat"] * persentase),
                "lemak": int(target_harian["lemak"] * persentase)
            }
        
        sarapan_resep, sarapan_fmt = dapatkan_atau_hasilkan_resep("sarapan", target_makan["sarapan"], info_pengguna)
        makan_siang_resep, makan_siang_fmt = dapatkan_atau_hasilkan_resep("makan siang", target_makan["makan_siang"], info_pengguna)
        makan_malam_resep, makan_malam_fmt = dapatkan_atau_hasilkan_resep("makan malam", target_makan["makan_malam"], info_pengguna)

        
        
        kalori_hari = sarapan_resep["kalori"] + makan_siang_resep["kalori"] + makan_malam_resep["kalori"]
        protein_hari = sarapan_resep["protein"] + makan_siang_resep["protein"] + makan_malam_resep["protein"]
        karbohidrat_hari = sarapan_resep["karbohidrat"] + makan_siang_resep["karbohidrat"] + makan_malam_resep["karbohidrat"]
        lemak_hari = sarapan_resep["lemak"] + makan_siang_resep["lemak"] + makan_malam_resep["lemak"]
        
        rencana_makan[hari] = {
            "sarapan": sarapan_resep,        # ✅ dict
            "makan_siang": makan_siang_resep,
            "makan_malam": makan_malam_resep,
            "format": {
                "sarapan": sarapan_fmt,
                "makan_siang": makan_siang_fmt,
                "makan_malam": makan_malam_fmt
            },
            "total": {
                "kalori": kalori_hari,
                "protein": protein_hari,
                "karbohidrat": karbohidrat_hari,
                "lemak": lemak_hari
            }
        }

    return rencana_makan, target_harian

def format_rencana_makan(rencana_makan, target_harian):
    teks_rencana = "📅 RENCANA MAKAN 7 HARI ANDA 📅\n\n"
    teks_rencana += f"Target Harian: {target_harian['kalori']} kalori, {target_harian['protein']:.0f}g protein, "
    teks_rencana += f"{target_harian['karbohidrat']:.0f}g karbohidrat, {target_harian['lemak']:.0f}g lemak\n\n"
    
    hari_list = []
    kalori_list = []
    protein_list = []
    karbohidrat_list = []
    lemak_list = []
    
    for hari, makan in rencana_makan.items():
        hari_list.append(hari.split(',')[0])
        kalori_list.append(makan["total"]["kalori"])
        protein_list.append(makan["total"]["protein"])
        karbohidrat_list.append(makan["total"]["karbohidrat"])
        lemak_list.append(makan["total"]["lemak"])
        
        teks_rencana += f"--- {hari} ---\n"
        teks_rencana += f"{makan['format']['sarapan']}\n"
        teks_rencana += f"{makan['format']['makan_siang']}\n"
        teks_rencana += f"{makan['format']['makan_malam']}\n"

        
        teks_rencana += f"Total Harian: {makan['total']['kalori']} kalori, "
        teks_rencana += f"{makan['total']['protein']}g protein, {makan['total']['karbohidrat']}g karbohidrat, {makan['total']['lemak']}g lemak\n\n"
    
    data_nutrisi = {
        'Hari': hari_list,
        'Kalori': kalori_list,
        'Protein (g)': protein_list,
        'Karbohidrat (g)': karbohidrat_list,
        'Lemak (g)': lemak_list
    }
    
    return teks_rencana, data_nutrisi

def buat_grafik_nutrisi(data_nutrisi):
    try:
        hari = data_nutrisi['Hari']
        kalori = data_nutrisi['Kalori']
        protein = data_nutrisi['Protein (g)']
        karbohidrat = data_nutrisi['Karbohidrat (g)']
        lemak = data_nutrisi['Lemak (g)']
        
        plt.switch_backend('Agg')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
        
        ax1.bar(hari, kalori, color='skyblue')
        ax1.set_title('Distribusi Kalori Harian')
        ax1.set_ylabel('Kalori')
        rata_kalori = sum(kalori)/len(kalori)
        ax1.axhline(rata_kalori, color='r', linestyle='--', 
                   label=f'Rata-rata: {rata_kalori:.0f} kal')
        ax1.legend()
        
        lebar = 0.25
        x = range(len(hari))
        ax2.bar([i - lebar for i in x], protein, lebar, label='Protein', color='salmon')
        ax2.bar(x, karbohidrat, lebar, label='Karbohidrat', color='lightgreen')
        ax2.bar([i + lebar for i in x], lemak, lebar, label='Lemak', color='gold')
        ax2.set_title('Rincian Makronutrien Harian')
        ax2.set_ylabel('Gram')
        ax2.set_xticks(x)
        ax2.set_xticklabels(hari)
        ax2.legend()
        
        plt.tight_layout()
        
        timestamp = time.strftime("%Y%m%d%H%M%S")
        nama_file = f"nutrisi_{timestamp}.png"
        plt.savefig(nama_file)
        plt.close(fig)
        
        return nama_file
        
    except Exception as e:
        print(f"Error membuat grafik: {e}")
        return None

def proses_input(input_pengguna):
    input_pengguna = input_pengguna.strip().lower()
    
    if input_pengguna == "reset":
        info_pengguna.update({"status": "awal", "kalori": 0, "persen_protein": 0, "persen_karbohidrat": 0, "persen_lemak": 0, "pembatasan": [], "alergi": []})
        return "🔄 Perencana menu direset!\n" + pesan_selamat_datang
    
    if input_pengguna == "keluar":
        return "👋 Terima kasih telah menggunakan PerencanaMenuPintar. Tetap sehat dan bahagia!"
    
    if input_pengguna == "bantuan":
        return pesan_bantuan
    
    if info_pengguna["status"] == "awal":
        if input_pengguna == "mulai":
            info_pengguna["status"] = "tanya_kalori"
            return "⚡ Mari kita mulai!\nBerapa kalori yang ingin Anda konsumsi setiap hari? (misalnya, 2000)"
        return "❓ Ketik **MULAI** untuk memulai perjalanan perencanaan makan Anda."
    
    elif info_pengguna["status"] == "tanya_kalori":
        try:
            kalori = int(input_pengguna)
            if kalori < 1200 or kalori > 4000:
                return "Harap masukkan target kalori harian yang wajar antara 1200 dan 4000 kalori."
            info_pengguna["kalori"] = kalori
            info_pengguna["status"] = "tanya_protein"
            return f"💪 Bagus! Sekarang, berapa persen kalori Anda yang harus berasal dari **protein**? (misalnya, 30)"
        except ValueError:
            return "🚫 Harap masukkan angka yang valid untuk kalori (misalnya, 2000)."
    
    elif info_pengguna["status"] == "tanya_protein":
        try:
            persen_protein = int(input_pengguna)
            if persen_protein < 10 or persen_protein > 50:
                return "Harap masukkan persentase protein yang wajar antara 10% dan 50%."
            info_pengguna["persen_protein"] = persen_protein
            info_pengguna["status"] = "tanya_karbohidrat"
            return f"🍞 Baik. Berapa persen yang harus berasal dari **karbohidrat**? (misalnya, 40)"
        except ValueError:
            return "🚫 Harap masukkan angka seperti 30."
    
    elif info_pengguna["status"] == "tanya_karbohidrat":
        try:
            persen_karbohidrat = int(input_pengguna)
            if persen_karbohidrat < 10 or persen_karbohidrat > 60:
                return "Harap masukkan persentase karbohidrat yang wajar antara 10% dan 60%."
            
            if info_pengguna["persen_protein"] + persen_karbohidrat > 100:
                return "⚠️ Total makro melebihi 100%. Coba persentase karbohidrat yang lebih rendah."
            
            info_pengguna["persen_karbohidrat"] = persen_karbohidrat
            info_pengguna["status"] = "tanya_lemak"
            sisa = 100 - info_pengguna["persen_protein"] - persen_karbohidrat
            return f"🥑 Dan {sisa}% sisanya untuk **lemak**. Silakan masukkan: {sisa}"
        except ValueError:
            return "🚫 Harap masukkan persentase yang valid."
    
    elif info_pengguna["status"] == "tanya_lemak":
        try:
            val = int(input_pengguna)
            total = info_pengguna["persen_protein"] + info_pengguna["persen_karbohidrat"] + val
            if total != 100:
                return f"⚠️ Total makro Anda harus sama dengan 100%. Anda memasukkan {total}%."
            info_pengguna["persen_lemak"] = val
            info_pengguna["status"] = "tanya_pembatasan"
            return "Bagus! Sekarang, apakah Anda memiliki pembatasan diet? (misalnya, vegetarian, vegan, bebas gluten, tidak ada)"
        except ValueError:
            return "🚫 Harap masukkan persentase lemak yang valid."
            
    elif info_pengguna["status"] == "tanya_pembatasan":
        if input_pengguna == "tidak ada":
            info_pengguna["pembatasan"] = []
        else:
            info_pengguna["pembatasan"] = [r.strip() for r in input_pengguna.split(",")]
        
        info_pengguna["status"] = "tanya_alergi"
        return "Baik! Apakah Anda memiliki alergi makanan? (misalnya, kacang, susu, telur, tidak ada)"
    
    elif info_pengguna["status"] == "tanya_alergi":
        if input_pengguna == "tidak ada":
            info_pengguna["alergi"] = []
        else:
            info_pengguna["alergi"] = [a.strip() for a in input_pengguna.split(",")]
        
        info_pengguna["status"] = "merencanakan"
        return "⏳ Bagus! Saya sedang menyiapkan rencana makan Anda menggunakan resep yang dihasilkan oleh AI... Ini mungkin membutuhkan waktu, karena saya sedang menghasilkan resep yang dipersonalisasi untuk Anda. 🍳(ketik: 'oke')"
    
    elif info_pengguna["status"] == "merencanakan":
        print("Menghasilkan rencana makan dengan API...")
        rencana_makan, target_harian = buat_rencana_makan(info_pengguna)
        teks_rencana, data_nutrisi = format_rencana_makan(rencana_makan, target_harian)
        nama_file_grafik = buat_grafik_nutrisi(data_nutrisi)
        
        info_pengguna["status"] = "selesai"
        
        respons = "✅ Rencana makan 7 hari yang dipersonalisasi untuk Anda sudah siap! 🎉\n\n"
        respons += "Saya telah membuat rencana makan yang dipersonalisasi berdasarkan persyaratan Anda:\n"
        respons += f"- Target Kalori Harian: {info_pengguna['kalori']} kalori\n"
        respons += f"- Makro: {info_pengguna['persen_protein']}% protein, {info_pengguna['persen_karbohidrat']}% karbohidrat, {info_pengguna['persen_lemak']}% lemak\n"
        
        if info_pengguna["pembatasan"]:
            respons += f"- Pembatasan Diet: {', '.join(info_pengguna['pembatasan'])}\n"
        if info_pengguna["alergi"]:
            respons += f"- Alergi Makanan: {', '.join(info_pengguna['alergi'])}\n"
        
        respons += "\n" + teks_rencana
        info_pengguna["teks_rencana"] = teks_rencana
        info_pengguna["file_grafik"] = nama_file_grafik
        
        if nama_file_grafik:
            respons += f"\nSaya juga telah membuat grafik nutrisi untuk membantu Anda memvisualisasikan rencana makan Anda. Grafik disimpan sebagai '{nama_file_grafik}'.\n\n"
            
        respons += "\n🔁 Ketik 'RESET' untuk membuat rencana lain atau 'KELUAR' untuk keluar."

        
        return "✉️ Apakah Anda ingin hasil ini dikirim ke email Anda? Jika ya, tuliskan email Anda di sini.\nAtau ketik 'tidak' untuk mengabaikan."
    
    elif info_pengguna["status"] == "selesai":
            if "@" in input_pengguna and "." in input_pengguna:
                success = kirim_email_ke_pengguna(input_pengguna, "Rencana Makan 7 Hari Anda", info_pengguna["teks_rencana"], info_pengguna.get("file_grafik"))
                if success:
                    info_pengguna["status"] = "email_terkirim"  # Ubah status setelah email berhasil
                    return "✅ Rencana makan berhasil dikirim ke email Anda!\n\n🔁 Ketik 'RESET' untuk membuat rencana baru atau 'KELUAR' untuk keluar."
                else:
                    return "❌ Gagal mengirim email. Pastikan email valid dan coba lagi."
            elif input_pengguna.lower() == "tidak":
                info_pengguna["status"] = "email_terkirim"  # Ubah status meskipun tidak mengirim email
                return "Oke, tidak ada email yang dikirim.\n\n🔁 Ketik 'RESET' untuk membuat rencana baru atau 'KELUAR' untuk keluar."
            else:
                return "Apakah Anda ingin mengirim hasil ini ke email Anda? Jika ya, ketik email Anda. Jika tidak, ketik 'tidak'."
        
    elif info_pengguna["status"] == "email_terkirim":
        # Status setelah email berhasil dikirim atau user memilih tidak mengirim
        if input_pengguna.lower() == "reset":
            info_pengguna.update({"status": "awal", "kalori": 0, "persen_protein": 0, "persen_karbohidrat": 0, "persen_lemak": 0, "pembatasan": [], "alergi": []})
            return "🔄 Perencana menu direset!\n" + pesan_selamat_datang
        elif input_pengguna.lower() == "keluar":
            return "👋 Terima kasih telah menggunakan PerencanaMenuPintar. Tetap sehat dan bahagia!"
        else:
            return "🔁 Ketik 'RESET' untuk membuat rencana makan baru atau 'KELUAR' untuk keluar."

    else:
        info_pengguna["status"] = "awal"
        return "⚠️ Terjadi kesalahan. Ketik 'RESET' untuk mencoba lagi."

def hasilkan_rencana_makan(input_pengguna):
    return proses_input(input_pengguna)
    
if __name__ == "__main__":
    print(pesan_selamat_datang)
