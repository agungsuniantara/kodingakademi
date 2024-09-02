#include<stdio.h>
void hasil(int nomer){
    int fact = 1;

    for(int i=1;i<=nomer;i++){
      fact=fact*i;
    }
    printf("Factorial of %d is: %d",nomer,fact);
}

int main(){
    int i, number;
    printf("Enter a number: ");
    scanf("%d",&number);
    hasil(number);

    return 0;
}
