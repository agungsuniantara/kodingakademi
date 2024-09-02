#include <stdio.h>

int main()
{
    int i, j, N;
    int tambah;

    printf("Enter N: ");
    scanf("%d", &N);

    for(i=1; i<= N; i++)
    {
        printf("%d", i);
        tambah = i;

        for(j=1; j<= N; j++)
        {
            tambah += 5;
            printf(" %d", tambah);
        }

        printf("\n");
    }
    return 0;
}
