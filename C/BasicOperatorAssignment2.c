#include <stdio.h>

int main(){
    float HargaMonitor = 150;
    float HargaKeyboard = 35;
    float BeliMonitor = 9;
    float BeliKeyboard = 9;
    float Total = (HargaMonitor * BeliMonitor) + (HargaKeyboard * BeliKeyboard);
    float Diskon;
    float TotalHarga;

    if(BeliMonitor >= 12 && BeliKeyboard <= 12){
        Diskon = (((HargaMonitor * BeliMonitor) + (HargaKeyboard * BeliKeyboard)) * 0.05);
        TotalHarga = Total - Diskon;
        printf("harga = $ %2.f", TotalHarga);
    }
    else if(BeliKeyboard >= 12 && BeliMonitor <= 12){
        Diskon = (((HargaMonitor * BeliMonitor) + (HargaKeyboard * BeliKeyboard)) * 0.03);
        TotalHarga = Total - Diskon;
        printf("harga = $ %2.f", TotalHarga);
    }
    else if(BeliMonitor >= 12 && BeliKeyboard >= 12){
        Diskon = (((HargaMonitor * BeliMonitor) + (HargaKeyboard * BeliKeyboard)) * 0.01);
        TotalHarga = Total - Diskon;
        printf("harga = $ %2.f", TotalHarga);
    }
    else{
        printf("harga = $ %2.f", Total);
    }

}
