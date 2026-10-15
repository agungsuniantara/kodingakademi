#include <iostream>
#include <string>
using namespace std;

struct Post {
    int likes;
    string post_name;
};

// Pass by value: menerima COPY (perubahan tidak terlihat pemanggil, mahal untuk struct besar)
void add_like_by_value(Post p) {
    p.likes += 1;
}

// Pass by reference: menerima variabel ASLI (perubahan terlihat pemanggil)
void add_like_by_ref(Post& p) {
    p.likes += 1;
}

// Pass by const reference: tidak copy, dan dijamin tidak mengubah (pola terbaik untuk read-only)
void print_post(const Post& p) {
    cout << p.post_name << " (" << p.likes << " likes)" << endl;
}

// Reference sebagai return: memungkinkan fungsi dipakai di sisi kiri '='
int& get_likes(Post& p) {
    return p.likes;
}

int main() {
    Post post = {10, "cat_video"};

    add_like_by_value(post);
    cout << "after by_value: " << post.likes << endl;   // tetap 10

    add_like_by_ref(post);
    cout << "after by_ref:   " << post.likes << endl;   // 11

    print_post(post);

    get_likes(post) = 50;   // menulis lewat reference yang dikembalikan
    cout << "after set:      " << post.likes << endl;   // 50

    // --- Perbandingan langsung: reference vs pointer ---
    int a = 1;
    int b = 2;

    int& ref = a;   // alias untuk a, wajib langsung diinisialisasi
    ref = 99;       // mengubah a
    cout << a << endl;  // 99

    int* ptr = &a;
    ptr = &b;       // pointer BOLEH diarahkan ulang (reference tidak bisa)
    *ptr = 77;      // mengubah b
    cout << b << endl;  // 77

    return 0;
}