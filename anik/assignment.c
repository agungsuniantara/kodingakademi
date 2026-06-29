#include <stdio.h>

void binary_search(int data[], int target, int n){
    int left = 0;
    int right = n - 1;
    int found = 0;

    while (left <= right){
        int mid = left + (right - left) / 2;
        if (data[mid] == target){
            printf("data ditemukan pada index %d \n", mid);
            found = 1;
            break;
        }
        else if (data[mid] < target){
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    if (!found){
        printf("data tidak ditemukan \n");
    }
}

int bubble_sort(int data[], int n){
    for (int i = 0; i < n-1; i++){
        for (int j = 0; j < n-i-1; j++){
            if (data[j] > data[j+1]){
                // swap
                int temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }
}

int main(){
    int data2[] = {5,3,8,6,2,7,4,1,10,9};
    int m = sizeof(data2) / sizeof(data2[0]);
    int target = 10;

    int hasil_bubble = bubble_sort(data2, m);

    printf("Data setelah diurutkan menggunakan bubble sort: \n ");
    for (int i = 0; i < m; i++){
        printf("%d ", data2[i]);
    }
    printf("\n");

    binary_search(data2, target, m);

    return 0;
}