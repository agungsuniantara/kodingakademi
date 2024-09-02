#include <stdio.h>

void menu(){
    printf("1. Insertion Sort\n");
    printf("2. Bubble Sort\n");
    printf("3. QuickSort\n");
    printf("4. Linear Search\n");
    printf("5. Binary Search\n");
    printf("0. Keluar \n");
}

void data(){
    printf("1. 1000 \n");
    printf("2. 16000 \n");
    printf("3. 32000 \n");
}

void insertionSort(int arr[], int n){
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

void bubbleSort(int arr[], int n){
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            // Bandingkan elemen saat ini dengan elemen berikutnya
            if (arr[j] > arr[j + 1]) {
                // Tukar elemen jika tidak dalam urutan yang benar
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Pilih elemen terakhir sebagai pivot
    int i = (low - 1); // Indeks dari elemen yang lebih kecil dari pivot

    for (int j = low; j <= high - 1; j++) {
        // Jika elemen saat ini lebih kecil dari atau sama dengan pivot
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Temukan indeks partisi, elemen yang ada di indeks ini sudah pada posisi yang benar
        int pi = partition(arr, low, high);

        // Pisahkan elemen sebelum dan sesudah partisi, dan urutkan rekursif kedua subarray
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++){
        if(arr[i] == target){
            printf("angka %d ditemukan pada array indeks ke-%d \n",target,i);
        }
    }
}

void binarySearch(int arr[], int n, int target){
    // bubble sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    //binary search
    int left = 0;
    int right = n - 1;
    int found = 0;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            printf("Elemen %d ditemukan pada indeks %d.\n", target, mid);
            found = 1;
            break;
        }

        if (arr[mid] > target) {
            right = mid - 1;
        }

        if (arr[mid] < target) {
            left = mid + 1;
        }
    }

    if (found == 0) {
        printf("Elemen %d tidak ditemukan dalam array.\n", target);
    }
}

void main(){
    printf("silahkan memilih menu berikut : \n");
    menu();

    int pilihan, masukan;

    printf("masukan pilihan : ");
    scanf("%d", &pilihan);

    if (pilihan == 1){
        data();
        printf("pilih data : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            insertionSort(array, jumlah_data);
        }
        else if(masukan == 2){
            int array[16000], i;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            insertionSort(array, jumlah_data);
        }
        else if(masukan == 3){
            int array[32000], i;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            insertionSort(array, jumlah_data);
        }
    }

    else if(pilihan == 2){
        data();
        printf("pilih data : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            bubbleSort(array, jumlah_data);
        }
        else if(masukan == 2){
            int array[16000], i;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            bubbleSort(array, jumlah_data);
        }
        else if(masukan == 3){
            int array[32000], i;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            bubbleSort(array, jumlah_data);
        }
    }

    else if(pilihan == 3){
        data();
        printf("pilih data : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            quickSort(array, 0, jumlah_data - 1);

            for (int i = 0; i < jumlah_data; i++){
                printf("%d ", array[i]);
            }
        }
        else if(masukan == 2){
            int array[16000], i;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            quickSort(array, 0, jumlah_data - 1);

            for (int i = 0; i < jumlah_data; i++){
                printf("%d ", array[i]);
            }
        }
        else if(masukan == 3){
            int array[32000], i;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            quickSort(array, 0, jumlah_data - 1);

            for (int i = 0; i < jumlah_data; i++){
                printf("%d ", array[i]);
            }
        }
    }

    else if(pilihan == 4){
        data();
        printf("pilih data : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i, target;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            linearSearch(array, jumlah_data, target);
        }
        else if(masukan == 2){
            int array[16000], i, target;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            linearSearch(array, jumlah_data, target);
        }
        else if(masukan == 3){
            int array[32000], i, target;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            linearSearch(array, jumlah_data, target);
        }
    }

    else if(pilihan == 5){
        data();
        printf("pilih data : ");
        scanf("%d", &masukan);

        if (masukan == 1){
            int array[1000], i, target;
            for (i = 0; i < 1000; i++){
                array[i] = rand()%1000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            binarySearch(array, jumlah_data, target);
        }
        else if(masukan == 2){
            int array[16000], i, target;
            for (i = 0; i < 16000; i++){
                array[i] = rand()%16000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            linearSearch(array, jumlah_data, target);
        }
        else if(masukan == 3){
            int array[32000], i, target;
            for (i = 0; i < 32000; i++){
                array[i] = rand()%32000;
            }

            int jumlah_data = sizeof(array) / sizeof(array[0]);

            printf("masukan target : ");
            scanf("%d", &target);

            linearSearch(array, jumlah_data, target);
        }
    }

    else if(pilihan == 0){
        printf("Sistem selesai !");
    }
}
