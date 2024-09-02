#include <stdio.h>

int main(){
    char data[] = "ini write fprintf";
    FILE *file = fopen("file.txt", "w");
    fprintf(file, "%s", data);
    fclose(file);
    return 0;
}
