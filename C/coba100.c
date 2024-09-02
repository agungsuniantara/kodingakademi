#include <stdio.h>

void main(){

     char *masukan = 'A';

     if(masukan >= 'a' && masukan <= 'z'){
        printf("huruf kecil");
        printf("\n");
        if (masukan == 'a'){
            printf("huruf vowel");
        }
        else if(masukan == 'i'){
            printf("huruf vowel");
        }
        else if(masukan == 'u'){
            printf("huruf vowel");
        }
        else if(masukan == 'e'){
            printf("huruf vowel");
        }
        else if(masukan == 'o'){
            printf("huruf vowel");
        }
        else {
            printf("huruf konsonan");
        }
     }
     else if(masukan >= 'A' && masukan <= 'Z'){
        printf("huruf besar");
        printf("\n");
        if (masukan == 'A'){
            printf("huruf vowel");
        }
        else if(masukan == 'I'){
            printf("huruf vowel");
        }
        else if(masukan == 'U'){
            printf("huruf vowel");
        }
        else if(masukan == 'E'){
            printf("huruf vowel");
        }
        else if(masukan == 'O'){
            printf("huruf vowel");
        }
        else {
            printf("huruf konsonan");
        }
     }
     else{
        printf("angka / tanda");
     }
}
