#include<iostream>
using namespace std;

int main()
{
    char kode;
    cout<<"Masukkan Kode Pegawai [A..C] : ";
    cin>>kode;

    switch(kode)
    {
        case 'A' :
            cout<<"Admin";
            break;
        case 'B' :
            cout<<"Bendahara";
            break;
        case 'C' :
            cout<<"Kasir";
            break;
        default:
            cout<<"Anda Salah Memasukan kode";
            break;
    } 
}