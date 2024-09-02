import pdb

def calculate(a, b):
    result = a + b
    pdb.set_trace()  # Set breakpoint di sini (catatan: n, s, l, c, q)
    return result

def main():
    x = 5
    y = 10
    z = calculate(x, y)
    print("Hasil:", z)

if __name__ == "__main__":
    main()

# Catatan:
# - Gunakan 'n' atau 'next' untuk melanjutkan eksekusi ke baris berikutnya.
# - Gunakan 's' atau 'step' untuk masuk ke dalam fungsi pada baris berikutnya.
# - Gunakan 'l' atau 'list' untuk menampilkan kode di sekitar posisi saat ini.
# - Gunakan 'c' atau 'continue' untuk melanjutkan eksekusi hingga menemukan breakpoint berikutnya atau selesai.
# - Gunakan 'q' atau 'quit' untuk keluar dari debugger dan berhenti menjalankan program.
