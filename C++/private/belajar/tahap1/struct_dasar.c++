#include <iostream>
#include <string>
using namespace std;

struct Post {
    int likes;
    string post_name;
};

// Struct bisa dikembalikan dari fungsi (pass by value = copy)
Post create_post(int likes, string name) {
    Post p;
    p.likes = likes;
    p.post_name = name;
    return p;
}

// Struct sebagai parameter (pass by reference agar tidak di-copy)
void print_post(const Post& p) {
    cout << "Post: " << p.post_name << " | Likes: " << p.likes << endl;
}

int main() {
    // Cara 1: inisialisasi langsung dengan {}
    Post p1 = {10, "cat_video"};

    // Cara 2: deklarasi lalu isi field satu per satu
    Post p2;
    p2.likes = 25;
    p2.post_name = "dog_video";

    // Cara 3: copy seluruh struct (semua field ikut ter-copy)
    Post p3 = p1;
    p3.likes = 99; // tidak mengubah p1

    print_post(p1);
    print_post(p2);
    print_post(p3);
    print_post(create_post(7, "meme"));

    return 0;
}