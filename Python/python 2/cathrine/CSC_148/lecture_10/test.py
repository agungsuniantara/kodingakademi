def find_min(arr):
    min_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
    return min_value

# Fungsi untuk menentukan batas atas (upper bound) dari waktu eksekusi algoritma

def upper_bound(arr):
    return len(arr)  # Big O (O) dari algoritma ini adalah O(n), karena ada satu loop yang bergantung pada ukuran input

# Fungsi untuk menentukan batas bawah (lower bound) dari waktu eksekusi algoritma
def lower_bound(arr):
    return 1  # Omega (ω) dari algoritma ini adalah Ω(1), karena algoritma memiliki kompleksitas waktu konstan

# Daftar input
arr = [9, 2, 5, 1, 7]

# Output minimum dari daftar
print("Nilai minimum:", find_min(arr))

# Output batas atas dan batas bawah waktu eksekusi algoritma
print("Batas atas waktu eksekusi:", upper_bound(arr))
print("Batas bawah waktu eksekusi:", lower_bound(arr))
