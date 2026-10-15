#include <iostream>

using namespace std;

int main(){

    int angka1, angka2;

    cout << "angka1 : ";
    cin >> angka1;

    cout << "angka2 : ";
    cin >> angka2;

    cout << "angka1 = " << angka1 << "\n";
    cout << "angka2 = " << angka2 << "\n";

    // operator (aritmatika, assignment, comparison, logika)

    // operator aritmatika (+, -, *, /, %)

    int tambah = angka1 + angka2;
    cout << "tambah = " << tambah << "\n";
    int kurang = angka1 - angka2;
    cout << "kurang = " << kurang << "\n";
    int kali = angka1 * angka2;
    cout << "kali = " << kali << "\n";
    int bagi = angka1 / angka2;
    cout << "tambah = " << tambah << "\n";
    int sisa_bagi = angka1 % angka2;
    cout << "sisa bagi = " << sisa_bagi << "\n";

    // operator assignment (+= , -=, *=, /=, %=)

    int contoh1 = 10;
    cout << "sebelum assign += :" << contoh1 << "\n";

    contoh1 += 20; // contoh1 = contoh1 + 20
    cout << "setelah assign += :" << contoh1 << "\n";

    contoh1 -= 40; // contoh1 = contoh1 - 40
    cout << "setelah assign -= :" << contoh1 << "\n";

    // operator comparison ( >, <, <=, >=, != , == )

    int number1 = 10;
    int number2 = 10;
    int number3 = 30;

    bool besar = number1 > number2;
    cout << "lebih besar = " << besar << "\n";
    bool kecil = number1 < number2;
    cout << "lebih kecil = " << besar << "\n";
    bool besar_sama = number1 >= number2;
    cout << "lebih besar sama dengan = " << besar_sama << "\n";
    bool kecil_sama = number1 <= number2;
    cout << "lebih kecil sama dengan = " << kecil_sama << "\n";
    bool tidak_sama = number1 != number2;
    cout << "tidak sama dengan = " << tidak_sama << "\n";
    bool sama = number1 == number2;
    cout << "sama dengan = " << sama << "\n";

    // operator logic ( and(&&), or(||), not(!) )
    // and = jika salah satu kondisi false hasilnya false
    // or = jika salah satu kondisi true hasilnya true
    // not / negasi = kebalikan, contoh awal true menjadi false

    int barang1 = 10;
    int barang2 = 20;
    int barang3 = 30;

    bool logika_and = (barang1 < barang2) && (barang2 > barang3);
    cout << "logika and = " << logika_and << "\n";

    bool logika_or = (barang1 < barang2) || (barang2 > barang3);
    cout << "logika or = " << logika_or << "\n";

    bool logika_not = !(barang1 < barang2) || (barang2 > barang3);
    cout << "logika not = " << logika_not << "\n";
}