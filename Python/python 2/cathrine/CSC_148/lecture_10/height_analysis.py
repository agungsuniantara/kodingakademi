def find_max_height(arr):
    if not arr:
        return None  # Mengembalikan None jika daftar kosong
    max_height = arr[0]  # Mengambil elemen pertama sebagai kandidat ketinggian tertinggi
    for height in arr:
        if height > max_height:
            max_height = height
    return max_height

# Contoh penggunaan:
heights = [170, 165, 180, 160, 175]
max_height = find_max_height(heights)
print("Ketinggian tertinggi:", max_height)

