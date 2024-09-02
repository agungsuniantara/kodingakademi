from queue import Queue

# Membuat objek queue
my_queue = Queue()

# Enqueue (menambah elemen)
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Dequeue (mengambil dan menghapus elemen paling depan)
print("Queue:")
print(my_queue.get())  # Output: 1
print(my_queue.get())  # Output: 2

# Ukuran queue
print("Ukuran Queue:", my_queue.qsize())  # Output: 1

# Cek apakah queue kosong
print("Queue Kosong:", my_queue.empty())  # Output: False

print("isi queue : ")
while not my_queue.empty():
    print(my_queue.get())
