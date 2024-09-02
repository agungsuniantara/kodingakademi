#include <stdio.h>

void main ()
{
    char mystring[6] = "manish"; // hanish // hanism
    char* ptr1[6];
    char* ptr2[6];
    char tampung[6]; // manish
    int i;

    for ( i = 0; i < 6; i++)
    {
        ptr1[i] = &mystring[i];
        ptr2[i] = &mystring[i];
        tampung[i] = mystring[i];
    }

    for ( i = 0; i < 6; i++)
    {
        if(i == 0){
            *ptr1[0] = tampung[5];
        }
        else if(i == 5){
            *ptr2[5] = tampung[0];
        }
    }

    for ( i = 0; i < 6; i++) {
        printf("%c", mystring[i]);
    }
}

