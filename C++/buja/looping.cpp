#include <iostream>

using namespace std;

int main(){

    // for 
    for (int i = 0; i < 5; i++){
        cout << i << "\n";
    }

    // for di dalam for
    for (int i = 0; i < 5; i++){
        for (int z = 10; z < 15; z++){
            cout << z;
        }
        cout << "\n";
    }

    // while
    int chance = 0;
    int kunci = 10;
    int answer;
    while (chance < 5){
        cout << "jawab : ";
        cin >> answer;

        if (answer == kunci){
            cout << "jawaban benar !!" << "\n";
            break;
        }
        else{
            cout << "jawaban salah !!" << "\n";
            chance += 1;
        }
    }

    cout << "\n";

    // do while
    int z = 0; 
    do {
        cout << z;
        z += 1;
    }while(z < 5);

    // perbedaan while dan do while

    int bensin = 9;

    while(bensin > 0){
        cout << "Masih ada bensin, nyalakan mesin!";
        bensin--;
    }

    do{
        cout << "Nyalakan mesin!";
        bensin--;
    } while(bensin > 0);

    return 0;
}