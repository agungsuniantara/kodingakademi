#include <iostream>

using namespace std;

main(){

    //buat variabel
    int detik, menit, jam, sisajam;

    //Input satuan waktu detik
    cout<<"Masukkan waktu dalam detik : ";cin>>detik;cout<<endl;

    //Proses konversi 
    jam=detik/3600;

    //Menghasilkan modulo
    sisajam=detik%3600; //Sisa bagi atau modulo

    //Menit adalah sisa dari perhitungan di atas
    menit=sisajam/60;

    //Detik adalah sisa dari perhitung di atas
    detik = sisajam%60;

    //Menampilkan hasil operasi
    cout<<"Waktu diatas setara dengan "<<jam<<" Jam, "<<menit<<" menit, "<<detik<<" detik"<<endl;
}