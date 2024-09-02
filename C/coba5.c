#include <stdio.h>

int main() {
    int n, tambah;

    printf("masukan kolom : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++){
        printf("%d", i);
        tambah = i;
        for (int x = 1; x <= n; x++){
            tambah += 5;
            printf(" %d", tambah);
        }
        printf("\n");
    }

   return 0;
}
