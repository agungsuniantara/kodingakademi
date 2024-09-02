#include <stdio.h>

int main() {
    char file[] = "file.txt";

    if (remove(file) == 0) {
        printf("File %s berhasil di hapus", file);
    } else {
        printf("Error menghapus file");
    }

    return 0;
}
