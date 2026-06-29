import streamlit as st
import pandas as pd
import pydeck as pdk
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "flora.csv"
FALLBACK_IMAGE = "assets/images/not_found.svg"

# --- NatureServe 2012 Rating-to-Points Mappings ---
RARITY_POINTS = {
    "A": 0.00, "B": 0.69, "C": 1.38, "D": 2.20,
    "E": 2.75, "F": 3.30, "G": 3.85, "H": 4.40, "I": 5.50,
}
THREAT_POINTS = {
    "A": 0.00, "B": 1.80, "C": 2.50, "D": 3.30,
    "E": 4.00, "F": 4.40, "G": 5.00, "H": 5.50,
}
TREND_POINTS = {
    "A": -0.57, "B": -0.44, "C": -0.31, "D": -0.22,
    "E": -0.14, "F": -0.07, "G": 0.00, "H": 0.22, "I": 0.44,
}

NS_WEIGHTS = {
    "re": 1.0, "ao": 2.0, "ps": 2.0, "no": 1.0, "gv": 2.0,
    "ti": 1.0,
}
TREND_WEIGHTS = {"st": 2.0, "lt": 1.0}

G_RANK_BOUNDARIES = [
    (1.5, "G1", "Critically Imperiled", 85, "🔴 KRITIS"),
    (2.5, "G2", "Imperiled", 70, "🟠 TINGGI"),
    (3.5, "G3", "Vulnerable", 50, "🟡 SEDANG"),
    (4.5, "G4", "Apparently Secure", 25, "🟢 RENDAH"),
    (5.5, "G5", "Secure", 0, "💚 AMAN"),
]


@st.cache_data
def load_flora_data():
    return pd.read_csv(DATA_FILE).to_dict("records")


def get_image_path(image_path):
    if not image_path:
        return FALLBACK_IMAGE
    if (BASE_DIR / image_path).exists():
        return image_path
    return FALLBACK_IMAGE


def _get_pt(val, mapping, default="C"):
    return mapping.get(str(val).strip().upper() if pd.notna(val) else default, mapping[default])


def calculate_natureserve_g_rank(tanaman):
    """Compute G-Score (0.0–5.5) using NatureServe 2012 10-factor methodology."""
    re_pt = _get_pt(tanaman.get("re"), RARITY_POINTS)
    ao_pt = _get_pt(tanaman.get("ao"), RARITY_POINTS)
    ps_pt = _get_pt(tanaman.get("ps"), RARITY_POINTS)
    no_pt = _get_pt(tanaman.get("no"), RARITY_POINTS)
    gv_pt = _get_pt(tanaman.get("gv"), RARITY_POINTS)
    ti_pt = _get_pt(tanaman.get("ti"), THREAT_POINTS)
    st_pt = _get_pt(tanaman.get("st"), TREND_POINTS)
    lt_pt = _get_pt(tanaman.get("lt"), TREND_POINTS)

    rarity_weighted = (re_pt * NS_WEIGHTS["re"]
                       + ao_pt * NS_WEIGHTS["ao"]
                       + ps_pt * NS_WEIGHTS["ps"]
                       + no_pt * NS_WEIGHTS["no"]
                       + gv_pt * NS_WEIGHTS["gv"])
    rarity_w_sum = sum(NS_WEIGHTS[k] for k in ("re", "ao", "ps", "no", "gv"))
    rarity_sub = rarity_weighted / rarity_w_sum

    threat_sub = ti_pt * NS_WEIGHTS["ti"] / NS_WEIGHTS["ti"]

    initial_score = (rarity_sub * 0.7) + (threat_sub * 0.3)

    trend_sub = (st_pt * TREND_WEIGHTS["st"] + lt_pt * TREND_WEIGHTS["lt"]) / sum(TREND_WEIGHTS.values())

    g_score = round(initial_score + trend_sub, 2)
    g_score = max(0.0, min(5.5, g_score))
    return g_score


def g_score_to_g_rank(g_score):
    for bound, g_rank, g_label, risk_base, _ in G_RANK_BOUNDARIES:
        if g_score <= bound:
            return g_rank, g_label, risk_base
    return "G5", "Secure", 0


def calculate_florapedia_risk_score(tanaman, g_score, risk_base):
    ns_normalized = ((5.5 - g_score) / 5.5) * 100
    endemik_val = 95 if tanaman.get("endemik") == "Ya" else 10
    ancaman_list = [a.strip() for a in str(tanaman.get("ancaman", "")).split(";") if a.strip()]
    ancaman_val = min(100, 10 + len(ancaman_list) * 20)
    dilindungi_val = 85 if tanaman.get("dilindungi") == "Ya" else 20
    aksi_val = min(50, len([a for a in str(tanaman.get("aksi_konservasi", "")).split(";") if a.strip()]) * 15)

    risk_score = round(
        (ns_normalized * 0.50)
        + (endemik_val * 0.20)
        + (ancaman_val * 0.20)
        + (dilindungi_val * 0.15)
        - (aksi_val * 0.05)
    )
    risk_score = max(0, min(100, risk_score))

    g_rank, g_label, _ = g_score_to_g_rank(g_score)

    if risk_score >= 80:
        prioritas = "Kritis"
    elif risk_score >= 60:
        prioritas = "Tinggi"
    elif risk_score >= 40:
        prioritas = "Sedang"
    else:
        prioritas = "Rendah"

    alasan = []
    if g_score <= 1.5:
        alasan.append(f"G-Rank {g_rank} ({g_label}) — sebaran sangat sempit")
    elif g_score <= 2.5:
        alasan.append(f"G-Rank {g_rank} ({g_label}) — risiko tinggi dari faktor NatureServe")
    if tanaman.get("endemik") == "Ya":
        alasan.append(f"Endemik {tanaman.get('pulau')}")
    if ancaman_list:
        alasan.append(f"Ancaman: {', '.join(ancaman_list[:2])}")

    return g_score, g_rank, g_label, risk_score, prioritas, alasan


def get_g_rank_color(g_rank):
    colors = {"G1": [220, 38, 38, 255], "G2": [245, 158, 11, 255],
              "G3": [234, 179, 8, 255], "G4": [34, 197, 94, 255],
              "G5": [22, 163, 74, 255]}
    return colors.get(g_rank, [150, 150, 150, 255])


DATA_FLORA = load_flora_data()
for flora in DATA_FLORA:
    gs = calculate_natureserve_g_rank(flora)
    g_rank, g_label, risk_base = g_score_to_g_rank(gs)
    ns, g_rank, g_label, flora["risk_score"], flora["prioritas"], flora["alasan_risk"] = \
        calculate_florapedia_risk_score(flora, gs, risk_base)
    flora["g_score"] = gs
    flora["g_rank"] = g_rank
    flora["g_label"] = g_label

# ==========================================
# 2. PENGATURAN HALAMAN & STATE MANAGEMENT
# ==========================================
st.set_page_config(page_title="Florapedia", page_icon="🌿", layout="wide")

# Menginisialisasi memori sesi untuk kuis
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'soal_selesai' not in st.session_state:
    st.session_state.soal_selesai = False

# ==========================================
# 3. NAVIGASI SIDEBAR
# ==========================================
st.sidebar.title("🌿 Florapedia")
menu = st.sidebar.radio("Navigasi Menu:", ["📖 Galeri Flora", "🗺️ Peta Persebaran", "🎮 Kuis Edukasi"])

st.sidebar.divider()
st.sidebar.info("Florapedia: Code to Preserve Life.")

# ==========================================
# 4. HALAMAN 1: GALERI FLORA (CARD LAYOUT)
# ==========================================
if menu == "📖 Galeri Flora":
    st.title("Galeri Flora Endemik")
    st.write("Jelajahi dan kenali tanaman langka yang menjadi kekayaan alam kita.")

    # Widget Filter Interaktif
    kolom_cari, kolom_filter = st.columns(2)
    with kolom_cari:
        kata_kunci = st.text_input("Cari nama tanaman:")
    with kolom_filter:
        pilihan_status = st.selectbox("Status Conservasi:", ["Semua", "Aman", "Rentan", "Terancam Punah"])

    st.divider()

    # Logika Pencarian
    hasil_pencarian = []
    for tanaman in DATA_FLORA:
        cocok_kata = kata_kunci.lower() in tanaman["nama"].lower() or kata_kunci == ""
        cocok_status = pilihan_status == "Semua" or tanaman["status"] == pilihan_status
        if cocok_kata and cocok_status:
            hasil_pencarian.append(tanaman)

    # Layout Kolom (Grid)
    if len(hasil_pencarian) > 0:
        kolom1, kolom2 = st.columns(2)
        for index, tanaman in enumerate(hasil_pencarian):
            kolom_tujuan = kolom1 if index % 2 == 0 else kolom2
            with kolom_tujuan:
                with st.expander(f"🌱 {tanaman['nama']}", expanded=True):
                    st.image(get_image_path(tanaman["gambar"]), use_container_width=True)
                    st.subheader(tanaman["nama"])
                    st.caption(f"_{tanaman['nama_ilmiah']}_")

                    col_badge, col_score = st.columns([1, 2])
                    with col_badge:
                        st.markdown(f"### {tanaman['g_rank']}")
                        st.caption(tanaman['g_label'])
                    with col_score:
                        st.metric("Conservation Risk Score (NatureServe)", f"{tanaman['risk_score']} / 100", tanaman["prioritas"])

                    st.caption(f"Habitat: {tanaman['habitat']} | Pulau: {tanaman['pulau']}")

                    if tanaman["status"] == "Terancam Punah":
                        st.error(f"Status: {tanaman['status']}")
                    elif tanaman["status"] == "Rentan":
                        st.warning(f"Status: {tanaman['status']}")
                    else:
                        st.success(f"Status: {tanaman['status']}")

                    st.write(f"**Alasan risiko:** {', '.join(tanaman['alasan_risk'])}")
                    st.write(f"**Aksi konservasi:** {tanaman['aksi_konservasi']}")
                    st.caption(f"Sumber: {tanaman['sumber']} | Confidence: {tanaman['confidence']} | G-Score: {tanaman['g_score']}")

                    st.write(tanaman["deskripsi"])
    else:
        st.warning("Tanaman tidak ditemukan.")

# ==========================================
# 5. HALAMAN 2: PETA GEOSPASIAL (LOGIKA GLOBAL AUTOMATIC OFFSET)
# ==========================================
elif menu == "🗺️ Peta Persebaran":
    st.title("Peta Habitat Flora")
    
    st.write("Lihat lokasi habitat alami flora endemik beserta garis penunjuk otomatis di bawah ini.")
    st.info("💡 Arahkan kursor (*hover*) tepat pada **Teks Nama Flora** atau **Titik Koordinat** untuk melihat detail tanaman.")
    
    filter_peta = st.selectbox("Tampilkan flora berdasarkan status:", ["Semua", "Aman", "Rentan", "Terancam Punah"], key="filter_peta")
    
    data_koordinat = []
    
    # Kunci Otomatisasi: Menggunakan urutan indeks yang lolos filter
    idx_lolos = 0
    for tanaman in DATA_FLORA:
        if filter_peta == "Semua" or tanaman["status"] == filter_peta:
            
            warna_rgb = get_g_rank_color(tanaman["g_rank"])

            # Mengatur letak teks mengambang agar tidak menumpuk secara zig-zag
            if idx_lolos % 2 == 0:
                hitung_teks_lat = tanaman["lat"] + 1.5
                hitung_teks_lon = tanaman["lon"] + 0.5
            else:
                hitung_teks_lat = tanaman["lat"] - 1.5
                hitung_teks_lon = tanaman["lon"] - 0.5
                
            data_koordinat.append({
                "nama_flora": tanaman["nama"],
                "status_konservasi": tanaman["status"],
                "g_rank": tanaman["g_rank"],
                "g_label": tanaman["g_label"],
                "risk_score": tanaman["risk_score"],
                "prioritas": tanaman["prioritas"],
                "lat": tanaman["lat"], 
                "lon": tanaman["lon"],
                "teks_lat": hitung_teks_lat,   
                "teks_lon": hitung_teks_lon,   
                "warna": warna_rgb,
                "gambar": get_image_path(tanaman["gambar"]),
                "deskripsi": tanaman["deskripsi"]
            })
            idx_lolos += 1
    
    if len(data_koordinat) > 0:
        df_peta = pd.DataFrame(data_koordinat)
        
        # --- LAYER 1: Garis Penunjuk ---
        layer_garis = pdk.Layer(
            "LineLayer",
            data=df_peta,
            get_source_position="[lon, lat]",             
            get_target_position="[teks_lon, teks_lat]",   
            get_color="[150, 150, 150, 200]",             
            get_width=1,
            pickable=False,
        )

        # --- LAYER 2: ScatterplotLayer (Titik Koordinat) ---
        layer_titik = pdk.Layer(
            "ScatterplotLayer",
            data=df_peta,
            get_position="[lon, lat]",
            get_fill_color="warna",
            get_radius=20000,   
            pickable=False,
        )
                
        # --- LAYER 3: TextLayer (Nama Flora Mengambang) ---
        layer_teks = pdk.Layer(
            "TextLayer",
            data=df_peta,
            get_position="[teks_lon, teks_lat]", 
            get_text="nama_flora",     
            get_color="warna",
            get_size=12,               
            get_alignment_baseline="'center'",
            font_weight="'bold'",
            pickable=True,             
        )

        # Mengatur posisi kamera awal peta
        kamera_peta = pdk.ViewState(
            latitude=-2.5,
            longitude=117.0,
            zoom=4,
            pitch=0
        )

        # Desain Struktur Tampilan Tooltip HTML saat di-hover
        html_tooltip = """
        <div style="font-family: Arial, sans-serif; padding: 8px; max-width: 260px; background-color: #ffffff; border-radius: 8px;">
            <h4 style="margin: 0 0 4px 0; color: #333;">{nama_flora}</h4>
            <p style="margin: 0 0 4px 0; font-size: 11px; color: #777;"><b>Status:</b> {status_konservasi}</p>
            <p style="margin: 0 0 4px 0; font-size: 11px; color: #777;"><b>G-Rank:</b> {g_rank} ({g_label})</p>
            <p style="margin: 0 0 8px 0; font-size: 11px; color: #777;"><b>Risk Score:</b> {risk_score}/100 ({prioritas})</p>
            <img src="{gambar}" style="width: 100%; max-height: 140px; object-fit: cover; border-radius: 6px; margin-bottom: 8px;" />
            <p style="margin: 0; font-size: 12px; color: #444; line-height: 1.4;">{deskripsi}</p>
        </div>
        """

        # Menampilkan Peta PyDeck ke Antarmuka
        st.pydeck_chart(
            pdk.Deck(
                map_style=None,
                initial_view_state=kamera_peta,
                layers=[layer_garis, layer_titik, layer_teks], 
                tooltip={
                    "html": html_tooltip,
                    "style": {
                        "backgroundColor": "white",
                        "color": "black",
                        "boxShadow": "0px 2px 6px rgba(0,0,0,0.3)",
                        "zIndex": "1000"
                    }
                }
            ),
            use_container_width=True
        )
    else:
        st.warning("Tidak ada data titik habitat untuk status tersebut.")

# ==========================================
# 6. HALAMAN 3: KUIS EDUKASI (STATE MANAGEMENT)
# ==========================================
elif menu == "🎮 Kuis Edukasi":
    st.title("Kuis Ekosistem")
    st.write("Uji pengetahuanmu tentang flora endemik!")

    if not st.session_state.soal_selesai:
        st.info("Jawab pertanyaan berikut untuk mendapatkan skor.")
        
        st.subheader("Pertanyaan 1:")
        st.write("Tanaman karnivora yang memakan serangga dan banyak ditemukan di Kalimantan adalah...")
        jawaban_1 = st.radio("Pilih jawaban:", ["Majegau", "Bunga Bangkai", "Kantong Semar"], key="j1")
        
        st.subheader("Pertanyaan 2:")
        st.write("Pohon yang kayunya sangat harum dan sering digunakan untuk kegiatan adat adalah...")
        jawaban_2 = st.radio("Pilih jawaban:", ["Majegau", "Bunga Sandat", "Pohon Jati"], key="j2")
        
        if st.button("Kirim Jawaban"):
            skor_sementara = 0
            if jawaban_1 == "Kantong Semar":
                skor_sementara += 50
            if jawaban_2 == "Majegau":
                skor_sementara += 50
                
            st.session_state.skor = skor_sementara
            st.session_state.soal_selesai = True
            st.rerun() 
            
    else:
        st.success("Kuis Selesai!")
        st.metric(label="Total Skor Kamu", value=f"{st.session_state.skor} / 100")
        
        if st.session_state.skor == 100:
            st.balloons()
            st.write("🌟 Sempurna! Kamu sangat peduli dengan keanekaragaman hayati kita.")
        elif st.session_state.skor >= 50:
            st.write("👍 Bagus! Mari kita pelajari lebih lanjut di halaman Galeri.")
        else:
            st.write("💪 Jangan menyerah, baca lagi deskripsi di Galeri dan coba lagi!")
            
        if st.button("Coba Lagi"):
            st.session_state.skor = 0
            st.session_state.soal_selesai = False
            st.rerun()
