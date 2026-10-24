#include <iostream>

using namespace std;

int main(){

    float gaji = 500000.0;
    int jam;
    int grade;
    float total;

    cout << "masukan grade : ";
    cin >> grade;

    cout << "masukan jam kerja : ";
    cin >> jam;

    if (grade == 1){
            
        int lembur = jam - 8;
        if (lembur > 8){
            total = gaji + gaji * 0.05 + lembur * 5000;
            cout << "total gaji : " << total << endl;
        }
        else{
            total = gaji + gaji * 0.05;
            cout << "total gaji : " << total << endl;
        }
    }
}