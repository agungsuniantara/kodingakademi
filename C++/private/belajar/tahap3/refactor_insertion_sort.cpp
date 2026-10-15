#include <iostream>
#include <string>
using namespace std;

// ===== Insertion Sort generik: bekerja untuk TANYA tipe dengan operator> =====
template <typename T>
void insertion_sort(T arr[], int size) {
    for (int i = 1; i < size; i++) {
        T key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

template <typename T>
void print_array(const T* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Struct custom: cukup definisikan operator> agar bisa disort
struct Post {
    int likes;
    string post_name;

    bool operator>(const Post& right) const {
        return likes > right.likes;
    }
};

int main() {
    int ints[5] = {5, 2, 9, 1, 6};
    insertion_sort(ints, 5);
    print_array(ints, 5);   // 1 2 5 6 9

    double doubles[4] = {3.5, 1.2, 4.8, 2.1};
    insertion_sort(doubles, 4);
    print_array(doubles, 4);   // 1.2 2.1 3.5 4.8

    string words[3] = {"pear", "apple", "orange"};
    insertion_sort(words, 3);
    print_array(words, 3);   // apple orange pear

    Post posts[4] = {
        {10, "cat_video"},
        {2,  "meme"},
        {25, "dog_video"},
        {7,  "dance_video"}
    };
    insertion_sort(posts, 4);
    for (int i = 0; i < 4; i++) {
        cout << posts[i].post_name << " (" << posts[i].likes << ")" << endl;
    }

    return 0;
}