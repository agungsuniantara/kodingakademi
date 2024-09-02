#include <stdio.h>

void main(){
    FILE *file;

    file = fopen("file.txt", "w");

    fclose(file);
}
