#include <iostream>
using namespace std;

main(){

    //Buat variabel
    double yard, kaki, inchi, meter;

    //Memasukkan nilai yard, kaki dan inchi
    cout<<"Input yard  : "; cin>>yard;
    cout<<"Input kaki  : "; cin>>kaki;
    cout<<"Input inchi : "; cin>>inchi;

    //Menghitung konversi
    meter = 0.9144*yard+0.3048*kaki+0.0254*inchi;cout<<endl;

    //Menampilkan hasil 
    cout<<yard<<" Yard, "<<kaki<<" Kaki, "<<inchi<<" Inchi adalah setara dengan "<<meter<<" meter"<<endl;
}