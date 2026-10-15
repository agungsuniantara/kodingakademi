#include <iostream>
#include <string>
using namespace std;

struct Post {
    int likes;
    string post_name;
};

// Post* yang dikembalikan dari fungsi ini AMAN,
// karena dialokasi dengan 'new' (di heap, bukan stack)
Post* create_single_post(int likes, string name) {
    Post* p = new Post{likes, name};
    return p;
}

// Deep copy: alokasi array BARU lalu salin isi satu per satu.
// Shallow copy (hanya menyalin alamat) berbahaya: 2 pointer
// menunjuk memori yang sama, delete ganda = crash.
Post* deep_copy_batch(const Post* source, int n) {
    Post* copy = new Post[n];
    for (int i = 0; i < n; i++) {
        copy[i].likes = source[i].likes;
        copy[i].post_name = source[i].post_name;
    }
    return copy;
}

int main() {
    // --- Pointer dasar ---
    int x = 42;
    int* ptr = &x;              // ptr menyimpan alamat x
    cout << *ptr << endl;       // dereference: 42
    *ptr = 100;                 // mengubah x lewat pointer
    cout << x << endl;          // 100

    // --- nullptr: pointer yang tidak menunjuk apa pun ---
    Post* nothing = nullptr;
    if (nothing == nullptr) {
        cout << "no post" << endl;
    }

    // --- Alokasi single object di heap ---
    Post* p = create_single_post(11, "dance_video");
    cout << p->likes << " " << p->post_name << endl;  // '->' = akses field via pointer
    delete p;                                          // wajib dibebaskan
    p = nullptr;                                       // hindari dangling pointer

    // --- Alokasi array di heap (persis pola scaffold C2) ---
    int n = 3;
    Post* batch = new Post[n];
    batch[0] = {4, "post_A"};
    batch[1] = {2, "post_B"};
    batch[2] = {10, "post_C"};

    // Deep copy sebelum sumber di-delete (skenario add_batch di C2)
    Post* stored = deep_copy_batch(batch, n);

    delete[] batch;   // scaffold meng-delete array aslinya
    batch = nullptr;

    // Data kita masih utuh karena sudah di-deep copy
    for (int i = 0; i < n; i++) {
        cout << stored[i].post_name << " (" << stored[i].likes << ")" << endl;
    }
    delete[] stored;  // array pakai delete[], single object pakai delete
    stored = nullptr;

    return 0;
}