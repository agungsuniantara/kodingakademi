#include <iostream>

using namespace std;

int main(){
    char balance[7] = "manish";
    
    char* ptr1 = balance;
    char* ptr2 = balance;

    for (int i = 0; i < 7; i++){
        if (i == 5){
            char first = balance[0];
            char last = balance[i];
            ptr1[i] = first;
            ptr2[0] = last;
        }
    }

    printf("%s", balance);
}