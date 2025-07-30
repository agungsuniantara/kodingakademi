// Sistem Manajemen Perpustakaan untuk Admin
#include <iostream>
#include <string>
using namespace std;

class Buku {
public:
    int id;
    string judul;
    string penulis;
    int tahun;

    Buku(int i, string j, string p, int t) : id(i), judul(j), penulis(p), tahun(t) {}
    void tampilkan() {
        cout << "ID: " << id << ", Judul: " << judul << ", Penulis: " << penulis << ", Tahun: " << tahun << endl;
    }
};

class Anggota {
public:
    string nama;
    int id;

    Anggota(string n, int i) : nama(n), id(i) {}
    void tampilkan() {
        cout << "Nama: " << nama << ", ID: " << id << endl;
    }
};

class Peminjaman {
public:
    Buku* buku;
    Anggota* anggota;
    string tanggal;
    Peminjaman* next;

    Peminjaman(Buku* b, Anggota* a, string t) : buku(b), anggota(a), tanggal(t), next(nullptr) {}
    void tampilkan() {
        cout << "Peminjaman: ";
        buku->tampilkan();
        cout << " Oleh: ";
        anggota->tampilkan();
        cout << " Tanggal: " << tanggal << endl;
    }
};

class RiwayatPeminjaman {
public:
    Peminjaman* head;

    RiwayatPeminjaman() : head(nullptr) {}

    void tambah(Buku* b, Anggota* a, string t) {
        Peminjaman* baru = new Peminjaman(b, a, t);
        if (!head) {
            head = baru;
        } else {
            Peminjaman* temp = head;
            while (temp->next) temp = temp->next;
            temp->next = baru;
        }
    }

    void tampilkan() {
        Peminjaman* temp = head;
        while (temp) {
            temp->tampilkan();
            cout << "-------------------------\n";
            temp = temp->next;
        }
    }

    ~RiwayatPeminjaman() {
        while (head) {
            Peminjaman* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    const int MAX_BUKU = 100, MAX_ANGGOTA = 50;
    Buku* daftarBuku[MAX_BUKU];
    Anggota* daftarAnggota[MAX_ANGGOTA];
    int jumlahBuku = 0, jumlahAnggota = 0;
    RiwayatPeminjaman riwayat;

    int pilihan;
    do {
        cout << "\n===== SISTEM MANAJEMEN PERPUSTAKAAN (Admin) =====\n";
        cout << "1. Tambah Buku\n";
        cout << "2. Tambah Anggota\n";
        cout << "3. Tampilkan Semua Buku\n";
        cout << "4. Tampilkan Semua Anggota\n";
        cout << "5. Lakukan Peminjaman\n";
        cout << "6. Lihat Riwayat Peminjaman\n";
        cout << "0. Keluar\n";
        cout << "Masukkan pilihan: ";
        cin >> pilihan;
        cin.ignore();

        if (pilihan == 1) {
            string judul, penulis;
            int tahun, id;
            cout << "ID Buku: "; cin >> id; cin.ignore();
            cout << "Judul buku: "; getline(cin, judul);
            cout << "Penulis: "; getline(cin, penulis);
            cout << "Tahun terbit: "; cin >> tahun;
            daftarBuku[jumlahBuku++] = new Buku(id, judul, penulis, tahun);
            cout << "Buku berhasil ditambahkan.\n";
        } else if (pilihan == 2) {
            string nama;
            int id;
            cout << "Nama anggota: "; getline(cin, nama);
            cout << "ID anggota: "; cin >> id;
            daftarAnggota[jumlahAnggota++] = new Anggota(nama, id);
            cout << "Anggota berhasil ditambahkan.\n";
        } else if (pilihan == 3) {
            cout << "\n--- Daftar Buku ---\n";
            for (int i = 0; i < jumlahBuku; ++i) daftarBuku[i]->tampilkan();
        } else if (pilihan == 4) {
            cout << "\n--- Daftar Anggota ---\n";
            for (int i = 0; i < jumlahAnggota; ++i) daftarAnggota[i]->tampilkan();
        } else if (pilihan == 5) {
            int idBuku, idAnggota;
            string tanggal;
            cout << "Masukkan ID Buku: "; cin >> idBuku;
            cout << "Masukkan ID Anggota: "; cin >> idAnggota;
            cin.ignore();
            cout << "Tanggal peminjaman (dd-mm-yyyy): "; getline(cin, tanggal);

            Buku* bukuPtr = nullptr;
            Anggota* anggotaPtr = nullptr;
            for (int i = 0; i < jumlahBuku; ++i) {
                if (daftarBuku[i]->id == idBuku) {
                    bukuPtr = daftarBuku[i];
                    break;
                }
            }
            for (int i = 0; i < jumlahAnggota; ++i) {
                if (daftarAnggota[i]->id == idAnggota) {
                    anggotaPtr = daftarAnggota[i];
                    break;
                }
            }
            if (bukuPtr && anggotaPtr) {
                riwayat.tambah(bukuPtr, anggotaPtr, tanggal);
                cout << "Peminjaman dicatat.\n";
            } else {
                cout << "ID Buku atau ID Anggota tidak ditemukan.\n";
            }
        } else if (pilihan == 6) {
            cout << "\n--- Riwayat Peminjaman ---\n";
            riwayat.tampilkan();
        }
    } while (pilihan != 0);

    for (int i = 0; i < jumlahBuku; ++i) delete daftarBuku[i];
    for (int i = 0; i < jumlahAnggota; ++i) delete daftarAnggota[i];

    return 0;
}
