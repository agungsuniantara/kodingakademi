#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// --- FUNGSI PENGURUTAN (SORTING) ---

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// --- FUNGSI PENCARIAN (SEARCHING) ---

int sequentialSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) return i;
    }
    return -1;
}

int binarySearch(int arr[], int n, int x) {
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (arr[m] == x) return m;
        if (arr[m] < x) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

// --- FUNGSI UTAMA ---

int main() {
    int pilihan, menuData, n;
    clock_t start, end;
    double cpu_time_used;

    while (1) {
        printf("\nPROGRAM PENGURUTAN DAN PENCARIAN\n");
        printf("1. Insertion Sort\n2. Bubble Sort\n3. Quicksort\n");
        printf("4. Sequential Search\n5. Binary Search\n0. keluar\n");
        printf("Masukkan pilihan anda : ");
        scanf("%d", &pilihan);

        if (pilihan == 0) break;

        printf("Menu yang disajikan\n1. 1000\n2. 16000\n3. 64000\n");
        printf("Masukkan pilihan : ");
        scanf("%d", &menuData);

        if (menuData == 1) n = 1000;
        else if (menuData == 2) n = 16000;
        else if (menuData == 3) n = 64000;
        else { printf("Pilihan tidak valid!\n"); continue; }

        // Alokasi memori dinamis untuk data besar
        int *data = (int*)malloc(n * sizeof(int));
        srand(time(NULL));
        for (int i = 0; i < n; i++) data[i] = rand() % 100000;

        if (pilihan >= 1 && pilihan <= 3) {
            printf("Mengurutkan %d data...\n", n);
            start = clock();
            if (pilihan == 1) insertionSort(data, n);
            else if (pilihan == 2) bubbleSort(data, n);
            else if (pilihan == 3) quickSort(data, 0, n - 1);
            end = clock();
        } 
        else if (pilihan == 4 || pilihan == 5) {
            int cari, hasil;
            printf("Masukkan angka yang dicari: ");
            scanf("%d", &cari);
            
            if (pilihan == 5) {
                printf("Catatan: Binary Search butuh data terurut. Mengurutkan dulu...\n");
                quickSort(data, 0, n - 1);
            }
            
            start = clock();
            hasil = (pilihan == 4) ? sequentialSearch(data, n, cari) : binarySearch(data, n, cari);
            end = clock();
            
            if (hasil != -1) printf("Data ditemukan pada indeks ke-%d\n", hasil);
            else printf("Data tidak ditemukan.\n");
        }

        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Waktu eksekusi: %f detik\n", cpu_time_used);

        free(data); // Bebaskan memori
    }

    return 0;
}