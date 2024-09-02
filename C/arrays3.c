#include <stdio.h>

int main(){
    int n,i,k,j;
    printf("enter length array : ");
    scanf("%d", &n);
    int p[n];

    printf("enter %d elements of array \n", n);

    for(i = 0; i <= n-1; i++){
        scanf("%d", &p[i]);
    }
    printf("the array is : ");
    printf("\n");

    for(i = 0; i <= n-1; i++){
        printf("%d\n", p[i]);
    }
    printf("enter position where to insert: ");
    scanf("%d", &k);

    for(j = n; j >= k; j--){
        p[j + 1] = p[j];
    }
    printf("\n enter the value to insert : ");
    scanf("%d", &p[k]);

    printf("\n array after insert: \n");
    for(i = 0; i <= n; i++){
        printf("%d\n",p[i]);
    }
}
