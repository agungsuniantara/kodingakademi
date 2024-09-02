#include <iostream>

using namespace std;

int main(){
    char balance[7] = "manish";
    
    char* ptr1 = balance;
    char* ptr2 = balance;

    for (int i = 0; i < 7; i++){
        if (i == 6){
            ptr1[i] = balance[0];
            ptr2[0] = balance[i];
        }
    }

    printf("%s", balance);
}