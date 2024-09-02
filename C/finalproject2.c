#include <stdio.h>

void menu(){
    printf("1. Insertion Sort\n");
    printf("2. Bubble Sort\n");
    printf("3. QuickSort\n");
    printf("4. Linear Search\n");
    printf("5. Binary Search\n");
    printf("0. Keluar \n");
}

void angka(){
    printf("1. 1000\n");
    printf("2. 16000\n");
    printf("3. 32000\n");
}

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Pindahkan elemen-elemen yang lebih besar dari key ke posisi lebih depan
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        // Tempatkan key pada posisi yang benar dalam array
        arr[j + 1] = key;
    }

    for (int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}

int linear_search(int arr[], int n, int target){
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

void binary_search(int arr[], int n, int target){
    // insertion sort
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Pindahkan elemen-elemen yang lebih besar dari key ke posisi lebih depan
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        // Tempatkan key pada posisi yang benar dalam array
        arr[j + 1] = key;
    }

    //binary search
    int left = 0;
    int right = n - 1;
    int found = 0;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Jika elemen tengah adalah target
        if (arr[mid] == target) {
            printf("Elemen %d ditemukan pada indeks %d.\n", target, mid);
            found = 1;
            break;
        }

        // Jika target lebih kecil, cari di setengah kiri dari mid
        if (arr[mid] > target) {
            right = mid - 1;
        }

        // Jika target lebih besar, cari di setengah kanan dari mid
        if (arr[mid] < target) {
            left = mid + 1;
        }
    }

    if (found == 0) {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }
}

void main(){
    menu();
    int pilihan, masukan;

    printf("masukan pilihan : ");
    scanf("%d", &pilihan);

    // insertion sort
    if (pilihan == 1){
        angka();
        printf("masukan pilihan angka : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
        else if (masukan == 2){
            int array[16000], i;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
        else if (masukan == 3){
            int array[32000], i;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
    }

    // bubble sort
     if (pilihan == 2){
        angka();
        printf("masukan pilihan angka : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
        else if (masukan == 2){
            int array[16000], i;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
        else if (masukan == 3){
            int array[32000], i;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
    }

    // linear search
     if (pilihan == 4){
        angka();
        printf("masukan pilihan angka : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i, target;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            int hasil = linear_search(array, n, target);

            if (hasil != -1){
                printf("Elemen %d ditemukan pada indeks %d.\n", target, hasil);
            }
            else{
                printf("Elemen %d tidak ditemukan dalam array.\n", target);
            }
        }
        else if (masukan == 2){
             int array[16000], i, target;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            int hasil = linear_search(array, n, target);

            if (hasil != -1){
                printf("Elemen %d ditemukan pada indeks %d.\n", target, hasil);
            }
            else{
                printf("Elemen %d tidak ditemukan dalam array.\n", target);
            }
        }
        else if (masukan == 3){
             int array[32000], i, target;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            int hasil = linear_search(array, n, target);

            if (hasil != -1){
                printf("Elemen %d ditemukan pada indeks %d.\n", target, hasil);
            }
            else{
                printf("Elemen %d tidak ditemukan dalam array.\n", target);
            }
        }
    }

    // binary search
     if (pilihan == 5){
        angka();
        printf("masukan pilihan angka : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i, target;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            binary_search(array, n, target);
        }
        else if (masukan == 2){
            int array[16000], i;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
        else if (masukan == 3){
            int array[32000], i;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }
            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
        }
    }

}
