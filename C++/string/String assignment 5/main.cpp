#include <iostream>
#include <string>
using namespace std;

int main(){
    string input;
    int total = 0;

    cout << "enter string: ";
    getline(cin,input);
    
    for(int i = 0; i < input.length(); i++){
        int ascii = static_cast<int>(input[i]);
        if(ascii > 47 && ascii < 58){
            int test = input[i] - '0';
            total += test;
        }
    }

    cout << total;
}
