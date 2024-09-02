#include <iostream>

using namespace std;

double getAverage(int *arr, int size);

int main(){
    int balance[5] = {1000, 2, 3, 17, 50};
    double avg;

    avg = getAverage(balance, 5);

    printf("Rata - rata : %f", avg);
}

double getAverage(int *arr, int size){
    double sum = 0;
    for (int i = 0; i < size; i++){
        sum += arr[i];
    }
    return sum / size;
}