#include<stdio.h>

void main(){
    int beli_monitor = 5;
    int beli_keyboard = 5;
    int harga_monitor = 150;
    int harga_keyboard = 35;

    if (beli_monitor >= 12){
        int total_monitor = beli_monitor * harga_monitor;
        int total_keyboard = beli_keyboard * harga_keyboard;
        int total_harga = total_monitor + total_keyboard;
        int diskon = total_harga * 0.05;
        int bayar = total_harga - diskon;
        printf("total pembayaran = %d", bayar);
    }
    else if(beli_keyboard >= 12){
        int total_monitor = beli_monitor * harga_monitor;
        int total_keyboard = beli_keyboard * harga_keyboard;
        int total_harga = total_monitor + total_keyboard;
        int diskon = total_harga * 0.03;
        int bayar = total_harga - diskon;
        printf("total pembayaran = %d", bayar);
    }
    else if(beli_monitor >= 12 && beli_keyboard >= 12){
        int total_monitor = beli_monitor * harga_monitor;
        int total_keyboard = beli_keyboard * harga_keyboard;
        int total_harga = total_monitor + total_keyboard;
        int diskon = total_harga * 0.01;
        int bayar = total_harga - diskon;
        printf("total pembayaran = %d", bayar);
    }
    else{
        int total_monitor = beli_monitor * harga_monitor;
        int total_keyboard = beli_keyboard * harga_keyboard;
        int total_harga = total_monitor + total_keyboard;
        printf("total pembayaran = %d", total_harga);
    }
}
