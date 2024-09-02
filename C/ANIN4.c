#include <stdio.h>

void main(){
    int harga_monitor = 150;
    int harga_keyboard = 35;
    int monitor = 10;
    int keyboard = 20;

    if (monitor >= 12){
        int total_monitor = harga_monitor * monitor;
        int total_keyboard = harga_keyboard * keyboard;
        int harga = total_monitor + total_keyboard
        int diskon = harga * 0.05;
        int total = harga - diskon;
        printf("total harga = %d", total);
    }
    else if (keyboard >= 12){
        int total_monitor = harga_monitor * monitor;
        int total_keyboard = harga_keyboard * keyboard;
        int harga = total_monitor + total_keyboard
        int diskon = harga * 0.03;
        int total = harga - diskon;
        printf("total harga = %d", total);
    }
    else if(monitor >= 12 && keyboard >= 12){
        int total_monitor = harga_monitor * monitor;
        int total_keyboard = harga_keyboard * keyboard;
        int harga = total_monitor + total_keyboard
        int diskon = harga * 0.01;
        int total = harga - diskon;
        printf("total harga = %d", total);
    }
}
