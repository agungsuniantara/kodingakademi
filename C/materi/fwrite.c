#include <stdio.h>

int main(){
    char kata[] = "ini write fwrite";
    FILE *file = fopen("file.txt", "w");
    fwrite(kata, sizeof(char), sizeof(kata), file);
    fclose(file);
    return 0;
}
