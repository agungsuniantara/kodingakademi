// ARCADE GAME CARD SYSTEM (E-MONEY)

// Teknis : 

// Struct: Tipe data Member berisi :

// 1. char id_kartu[20] (Sebagai Login)
// char nama[50]
// int saldo (Uang untuk main)
// int tiket (Hadiah yang dikumpulkan)

// 2. Pointer (Double Update):
// Fungsi mainGame harus menerima dua pointer: int *saldo dan int *tiket.
// Saat main, saldo dikurangi harga game, dan tiket ditambah sesuai skor.

// 3. File Handling:
// member.txt (Mode Write): Menyimpan data terakhir.
// history_main.txt (Mode Append): Mencatat game apa yang dimainkan.

// 4. Validasi: Tidak bisa main jika saldo kurang.

// spesifikasi : 

// 1. Login Kartu (ID Check)
// User diminta memasukkan ID Kartu.
// Bandingkan dengan data di file/struct.
// Jika ID benar, masuk ke menu utama.

// 2. Top Up Saldo
// Mirip fitur "Setor Tunai" di ATM.
// Menambah saldo user.
// Catat di history: TOPUP: +Rp [jumlah].

// 3. Main Game (The Core Feature)
// Sediakan pilihan game dengan harga dan hadiah berbeda:

// A. Mesin Capit Boneka: Harga Rp 5.000 (Dapat 0 - 50 Tiket secara acak/tetap).
// B. Balapan Mobil: Harga Rp 10.000 (Dapat 100 Tiket).
// C. Tembak Zombie: Harga Rp 7.000 (Dapat 50 Tiket).
// Logika Pointer:
// Saat user memilih game, panggil fungsi (contoh): prosesMain(&user.saldo, &user.tiket, harga, hadiah);

// Di dalam fungsi: Cek apakah *saldo >= harga.
// Jika ya: *saldo = *saldo - harga DAN *tiket = *tiket + hadiah.
// Jika tidak: Tampilkan "Saldo Kurang".

// 4. Tukar Hadiah (Exchange)
// Menu untuk menukar Tiket dengan Barang.
// Contoh: "Boneka" harga 500 Tiket.
// Logika: Cek apakah tiket >= 500. Jika ya, kurangi tiket.
// Catat di history: TUKAR: -500 Tiket (Boneka).

// 5. Cek Info & Riwayat
// Tampilkan Saldo sisa dan Jumlah Tiket yang dimiliki.
// Baca file history_main.txt dan tampilkan ke layar.

// alur sistem : 

// Data Awal:
// ID: USER001 | Saldo: 20.000 | Tiket: 0

// 1. Main Game:
// User pilih "Balapan Mobil" (Harga 10.000, Hadiah 100 Tiket).
// Program cek saldo (20.000 > 10.000) -> OK.
// Update: Saldo jadi 10.000, Tiket jadi 100.
// Log: MAIN: Balapan Mobil (-10.000)

// 2. Main Game Lagi:
// User pilih "Balapan Mobil" lagi.
// Program cek saldo (10.000 >= 10.000) -> OK.
// Update: Saldo jadi 0, Tiket jadi 200.
// Log: MAIN: Balapan Mobil (-10.000)

// 3. Tukar Hadiah:
// User ingin tukar "Permen" (Harga 50 Tiket).
// Program cek tiket (200 >= 50) -> OK.
// Update: Tiket sisa 150.

// 4. Simpan & Keluar:
// File member.txt diperbarui dengan data: Saldo 0, Tiket 150.

