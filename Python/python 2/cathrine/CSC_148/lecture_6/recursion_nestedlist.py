def nested_list_sum(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += nested_list_sum(element)  # Jika elemen adalah nested list, rekursif mencari jumlahnya
        else:
            total += element  # Jika elemen adalah angka, tambahkan ke total
    return total

# Contoh nested list
my_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]

# Panggil fungsi untuk menghitung jumlah semua elemen dalam nested list
result = nested_list_sum(my_list)
print("Jumlah semua elemen dalam nested list adalah:", result)
