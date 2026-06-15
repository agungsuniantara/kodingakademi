import json

KNOWLEDGE_BASE = {
    "bagaimana kendaraan bermotor menyebabkan emisi karbon": "Kendaraan bermotor membakar bahan bakar fosil (bensin/diesel), melepaskan gas buang seperti karbon dioksida (CO2) dan gas rumah kaca lainnya yang berkontribusi pada pemanasan global.",
    "berapa kontribusi sektor transportasi terhadap emisi nasional": "Di Indonesia, sektor transportasi merupakan salah satu penyumbang emisi karbon terbesar. Menurut data, kontribusinya bisa mencapai sekitar 20-25% dari total emisi nasional, terutama dari penggunaan kendaraan pribadi.",
    "bagaimana cara mengurangi jejak karbon perjalanan saya": "Untuk mengurangi jejak karbon perjalanan Anda, pertimbangkan untuk beralih ke transportasi umum (bus, kereta), bersepeda, berjalan kaki, atau menggunakan kendaraan listrik/hybrid jika memungkinkan. Menggabungkan perjalanan dan mengemudi secara efisien juga membantu.",
    "apa dampak jika saya beralih dari motor ke transportasi publik selama setahun": "Jika Anda beralih dari motor ke transportasi publik selama setahun, Anda dapat mengurangi emisi CO2 secara signifikan, menghemat biaya bahan bakar, mengurangi kemacetan, dan berkontribusi pada udara yang lebih bersih. Estimasi pengurangan emisi bisa mencapai ratusan kilogram CO2 per tahun, tergantung jarak tempuh.",
    "apa itu emisi karbon": "Emisi karbon adalah pelepasan gas karbon ke atmosfer bumi, terutama karbon dioksida (CO2), yang sebagian besar dihasilkan dari pembakaran bahan bakar fosil oleh aktivitas manusia dan menjadi penyebab utama perubahan iklim.",
    "dampak emisi karbon bagi lingkungan": "Dampak emisi karbon antara lain pemanasan global, perubahan iklim ekstrem (banjir, kekeringan), kenaikan permukaan air laut, kerusakan ekosistem laut (pemutihan karang), dan masalah kesehatan akibat polusi udara.",
    "tips transportasi berkelanjutan": "Tips transportasi berkelanjutan meliputi: gunakan angkutan umum, bersepeda atau berjalan kaki untuk jarak dekat, pertimbangkan kendaraan listrik, manfaatkan carpooling, dan rawat kendaraan Anda agar efisien bahan bakar.",
    "definisi perubahan iklim": "Perubahan iklim adalah pergeseran signifikan dan jangka panjang dalam pola cuaca global atau regional, terutama disebabkan oleh peningkatan konsentrasi gas rumah kaca di atmosfer akibat aktivitas manusia."
}

json_data = json.dumps(KNOWLEDGE_BASE, ensure_ascii=False, indent=2)
print(json_data)