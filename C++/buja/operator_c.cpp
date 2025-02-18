#include <iostream>

using namespace std;

int main(){
    int a, b;

    cout << "angka 1 : ";
    cin >> a;

    cout << "angka 2 : ";
    cin >> b; 

    int tambah = a + b; 
    cout << "tambah = " << tambah << "\n";
    int kurang = a - b; 
    cout << "kurang = " << kurang << "\n";
    int bagi = a / b; 
    cout << "bagi = " << bagi << "\n";
    int kali = a * b; 
    cout << "kali = " << kali << "\n";
    int modulo = a % b; 
    cout << "modulo = " << modulo << "\n";

    bool lebih_kecil = a < b;
    cout << "lebih kecil = " << lebih_kecil << "\n";
    bool lebih_besar = a > b;
    cout << "lebih besar = " << lebih_kecil << "\n";
    bool sama_dengan = a == b;
    cout << "sama dengan = " << sama_dengan << "\n";
    bool kecil_sama = a <= b;
    cout << "lebih kecil sama dengan = " << kecil_sama << "\n";
    bool besar_sama = a >= b;
    cout << "lebih besar sama dengan = " << kecil_sama << "\n";
    bool tidak_sama = a != b;
    cout << "tidak sama dengan = " << tidak_sama << "\n";

    int c;

    cout << "angka 3 : ";
    cin >> c;

    bool logika_and = (a < b) && (a > c);
    cout << "logika and : " << logika_and << "\n";

    bool logika_or = (a < b) || (a > c);
    cout << "logika or : " << logika_or << "\n";

    bool logika_negasi = !(a < b) || (a > c);
    cout << "logika negasi : " << logika_negasi << "\n";

    int z = 0;

    z += 10; // z = z + 10
    cout << "z = " << z << "\n";
    z -= 2; // z = z - 2
    cout << "z = " << z << "\n";
    z *= 1; // z = z + 1
    cout << "z = " << z << "\n";

    return 0;
}