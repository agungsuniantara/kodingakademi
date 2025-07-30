#include <iostream>
using namespace std;

string nama[20] = {};
string status[20] = {};
int gaji[20] = {};
int tahun[20] = {};
int jumlah = 0;  // Jumlah data pegawai saat ini

// Fungsi untuk mencari indeks berdasarkan nama
int cari_index(string n) {
    for (int i = 0; i < jumlah; i++) {
        if (nama[i] == n) {
            return i;
        }
    }
    return -1;  // Jika tidak ditemukan
}

void tambah_data(string a, string b, int c, int d) {
    if (jumlah < 20) {
        nama[jumlah] = a;
        status[jumlah] = b;
        gaji[jumlah] = c;
        tahun[jumlah] = d;
        jumlah++;
        cout << "Data berhasil ditambahkan!\n";
    } else {
        cout << "Data melebihi kapasitas\n";
    }
}

void edit_data(string n, string a, string b, int c, int d) {
    int index = cari_index(n);
    if (index != -1) {
        nama[index] = a;
        status[index] = b;
        gaji[index] = c;
        tahun[index] = d;
        cout << "Data pegawai berhasil diperbarui!\n";
    } else {
        cout << "Pegawai dengan nama '" << n << "' tidak ditemukan!\n";
    }
}

void hapus_data(string n) {
    int index = cari_index(n);
    if (index != -1) {
        for (int i = index; i < jumlah - 1; i++) {
            nama[i] = nama[i + 1];
            status[i] = status[i + 1];
            gaji[i] = gaji[i + 1];
            tahun[i] = tahun[i + 1];
        }
        jumlah--;
        cout << "Data pegawai berhasil dihapus!\n";
    } else {
        cout << "Pegawai dengan nama '" << n << "' tidak ditemukan!\n";
    }
}

void tampil_data() {
    if (jumlah == 0) {
        cout << "Belum ada data pegawai.\n";
        return;
    }

    for (int i = 0; i < jumlah; i++) {
        cout << "Data " << i + 1 << ":\n";
        cout << "Nama   : " << nama[i] << endl;
        cout << "Status : " << status[i] << endl;
        cout << "Gaji   : " << gaji[i] << endl;
        cout << "Tahun  : " << tahun[i] << endl;
        cout << "------------------------\n";
    }
}

void menu() {
    cout << "\nSelamat datang di sistem informasi pegawai\n";
    cout << "Silahkan memilih menu:\n";
    cout << "1. Tambah pegawai\n";
    cout << "2. Edit pegawai\n";
    cout << "3. Hapus pegawai\n";
    cout << "4. Tampil pegawai\n";
    cout << "5. Keluar sistem\n";
}

int main() {
    while (true) {
        int pilihan, g, t;
        string n, s, cari;

        menu();
        cout << "Pilih menu: ";
        cin >> pilihan;

        if (pilihan == 1) {
            cin.ignore();
            cout << "Masukkan nama   : ";
            getline(cin, n);
            cout << "Masukkan status : ";
            getline(cin, s);
            cout << "Masukkan gaji   : ";
            cin >> g;
            cout << "Masukkan tahun  : ";
            cin >> t;
            tambah_data(n, s, g, t);
        } else if (pilihan == 2) {
            cin.ignore();
            cout << "Masukkan nama pegawai yang ingin diedit: ";
            getline(cin, cari);
            cout << "Masukkan nama baru   : ";
            getline(cin, n);
            cout << "Masukkan status baru : ";
            getline(cin, s);
            cout << "Masukkan gaji baru   : ";
            cin >> g;
            cout << "Masukkan tahun baru  : ";
            cin >> t;
            edit_data(cari, n, s, g, t);
        } else if (pilihan == 3) {
            cin.ignore();
            cout << "Masukkan nama pegawai yang ingin dihapus: ";
            getline(cin, cari);
            hapus_data(cari);
        } else if (pilihan == 4) {
            tampil_data();
        } else if (pilihan == 5) {
            cout << "Terima kasih!\n";
            break;
        } else {
            cout << "Pilihan tidak valid!\n";
        }
    }
    return 0;
}
