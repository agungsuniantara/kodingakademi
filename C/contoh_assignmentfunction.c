# include <stdio.h>

int faktor(int angka){
    int hasil = 1;

    for (int i = angka; i > 1; i--) {
        hasil *= i;
    }

    return hasil;
}

int main(){
    int nomer = printf("masukkan angka : ");
    scanf("%d", &nomer);

    int hasil = faktor(nomer);

    printf("hasil pangkat %d adalah %d", nomer, hasil);
}
