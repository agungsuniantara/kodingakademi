#include <iostream>

using namespace std;

double luasPersegi(double sisi) {
    return sisi * sisi;
}

double luasPersegiPanjang(double panjang, double lebar) {
    return panjang * lebar;
}

double luasLingkaran(double jariJari) {
    return 3.14 * jariJari * jariJari;
}

double volumeKubus(double sisi) {
    return luasPersegi(sisi) * sisi;
}

double volumeBalok(double panjang, double lebar, double tinggi) {
    return luasPersegiPanjang(panjang, lebar) * tinggi;
}

double volumeTabung(double jariJari, double tinggi) {
    return luasLingkaran(jariJari) * tinggi;
}

char* pointer(char* word){
    char* ptr1 = word;
    char* ptr2 = word;

    int len = strlen(word);

    if (len >= 2){  
        char first = word[0]; 
        char last = word[len - 1];  

        ptr1[len - 1] = first;   
        ptr2[0] = last;    
    }

    return word;
}

int main() {
    bool kondisi = true;
    int pilihan;
    char word[100];

    while(true){
        cout << "Pilih sistem:\n";
        cout << "1. Sistem pointer\n";
        cout << "2. Sistem luas & volume\n";
        cout << "3. Selesai\n";
        cout << "Pilihan anda: ";
        cin >> pilihan;

        if (pilihan == 1) {
            cout << "Masukkan kata: ";
            cin >> word;
            cout << "Hasil = " << pointer(word) << endl;
        }
        else if(pilihan == 2){
            while(kondisi){
                int pilihan;
                cout << "Pilih bangun datar atau bangun ruang:\n";
                cout << "1. Luas Persegi\n";
                cout << "2. Luas Persegi Panjang\n";
                cout << "3. Luas Lingkaran\n";
                cout << "4. Volume Kubus\n";
                cout << "5. Volume Balok\n";
                cout << "6. Volume Tabung\n";
                cout << "7. Keluar\n";
                cout << "Pilihan Anda: ";
                cin >> pilihan;

                switch (pilihan) {
                    case 1: {
                        double sisi;
                        cout << "Masukkan panjang sisi persegi: ";
                        cin >> sisi;
                        cout << "Luas persegi: " << luasPersegi(sisi) << endl;
                        break;
                    }
                    case 2: {
                        double panjang, lebar;
                        cout << "Masukkan panjang persegi panjang: ";
                        cin >> panjang;
                        cout << "Masukkan lebar persegi panjang: ";
                        cin >> lebar;
                        cout << "Luas persegi panjang: " << luasPersegiPanjang(panjang, lebar) << endl;
                        break;
                    }
                    case 3: {
                        double jariJari;
                        cout << "Masukkan jari-jari lingkaran: ";
                        cin >> jariJari;
                        cout << "Luas lingkaran: " << luasLingkaran(jariJari) << endl;
                        break;
                    }
                    case 4: {
                        double sisi;
                        cout << "Masukkan panjang sisi kubus: ";
                        cin >> sisi;
                        cout << "Volume kubus: " << volumeKubus(sisi) << endl;
                        break;
                    }
                    case 5: {
                        double panjang, lebar, tinggi;
                        cout << "Masukkan panjang balok: ";
                        cin >> panjang;
                        cout << "Masukkan lebar balok: ";
                        cin >> lebar;
                        cout << "Masukkan tinggi balok: ";
                        cin >> tinggi;
                        cout << "Volume balok: " << volumeBalok(panjang, lebar, tinggi) << endl;
                        break;
                    }
                    case 6: {
                        double jariJari, tinggi;
                        cout << "Masukkan jari-jari tabung: ";
                        cin >> jariJari;
                        cout << "Masukkan tinggi tabung: ";
                        cin >> tinggi;
                        cout << "Volume tabung: " << volumeTabung(jariJari, tinggi) << endl;
                        break;
                    }
                    case 7: {
                        kondisi = false;
                        cout << "Program selesai" << endl;
                        break;
                    }
                    default:
                        cout << "Pilihan tidak valid!" << endl;
                        break;
                }
            }
        }
        else if(pilihan == 3){
            cout << "Sistem keluar !! " << endl;
            return 0;
        }
    }

    
    return 0;
}
