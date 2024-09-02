# contoh 1

try:
    x = int(input("Masukkan angka: "))
    hasil = 10 / x
    print("Hasil pembagian: ", hasil)
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diizinkan.")
except ValueError:
    print("Error: Input harus berupa angka.")
except Exception as e:
    print("Error:", e)

# contoh 2

try:
    num1 = int(input("Masukkan angka pertama: "))
    num2 = int(input("Masukkan angka kedua: "))
    result = num1 / num2
    print("Hasil pembagian:", result)
except ValueError:
    print("Input harus berupa angka.")
except ZeroDivisionError:
    print("Tidak dapat membagi angka dengan nol.")
else:
    print("Operasi berhasil.")
finally:
    print("Program selesai.")
