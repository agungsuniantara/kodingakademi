#include <iostream>
#include <string>
using namespace std;

struct Post {
    int likes;
    string post_name;

    bool operator<(const Post& right) const {
        return likes < right.likes;
    }

    bool operator>(const Post& right) const {
        return likes > right.likes;
    }
};

void insertion_sort(Post arr[], int size) {
    for (int i = 1; i < size; i++) {
        Post key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {   // butuh operator>
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
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