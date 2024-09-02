#include <stdio.h>

void main(){
    FILE *file;

    file = fopen("write.txt", "w");

    fprintf(file, "ini write printf");

    fclose(file);
}
