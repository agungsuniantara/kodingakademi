#include <stdio.h>

int main() {
    char *nama = "ttttt";

    int size = sizeof(nama);

    for (int i=0; i < size ; i++){
        if (nama[i] == 'a' || nama[i] == 'i' || nama[i] == 'u' || nama[i] == 'e' || nama[i] == 'o'){
            printf("huruf vokal");
            break;
        }
        else if (nama[i] == 'A' || nama[i] == 'I' || nama[i] == 'U' || nama[i] == 'E' || nama[i] == 'O'){
            printf("huruf vokal");
            break;
        }
        else{
            printf("huruf konsonan");
            break;
        }
    }
}
