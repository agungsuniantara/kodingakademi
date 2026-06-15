#include <stdio.h>

int selection_sort(int arr[], int n);
int bubble_sort(int arr[], int n);
int linear_search(int target, int data[], int n);
int binary_search(int target, int data[], int n);

int main(){
    printf("PROGRAM PENCARIAN DAN PENGURUTAN DATA\n");

    while (1){
        printf("\nMenu:\n");
        printf("1. selection sort\n");
        printf("2. bubble sort\n");
        printf("3. linear search\n");
        printf("4. binary search\n");
        printf("5. exit\n");

        int choice;

        printf("Pilih menu (1-5): ");
        scanf("%d", &choice);

        if (choice == 1){
            int array_choice;
            printf("Pilih jumlah angka array: ");
            printf("1. 1000");
            printf("2. 16000");
            printf("3. 64000");

            scanf("%d", &array_choice);
            if (array_choice == 1){
                int data[1000];

                for (int i = 0; i < 1000; i++){
                    data[i] = rand() % 10000;
                }

                selection_sort(data, 1000);
                printf("Data setelah diurutkan menggunakan selection sort: \n ");
                for (int i = 0; i < 1000; i++){
                    printf("%d ", data[i]);
                }
            } else if (array_choice == 2){
                int data[16000];

                for (int i = 0; i < 16000; i++){
                    data[i] = rand() % 10000;
                }

                selection_sort(data, 16000);
                printf("Data setelah diurutkan menggunakan selection sort: \n ");
                for (int i = 0; i < 16000; i++){
                    printf("%d ", data[i]);
                }
            } else if (array_choice == 3){
                int data[64000];

                for (int i = 0; i < 64000; i++){
                    data[i] = rand() % 10000;
                }

                selection_sort(data, 64000);
                printf("Data setelah diurutkan menggunakan selection sort: \n ");
                for (int i = 0; i < 64000; i++){
                    printf("%d ", data[i]);
                }
            } else {
                printf("Pilihan tidak valid.\n");
            }
        }
        else if (choice == 2){
            int array_choice;
            printf("Pilih jumlah angka array: ");
            printf("1. 1000");
            printf("2. 16000");
            printf("3. 64000");

            scanf("%d", &array_choice);
            if (array_choice == 1){
                int data[1000];
                for (int i = 0; i < 1000; i++){
                    data[i] = rand() % 10000;
                }
                bubble_sort(data, 1000);
                printf("Data setelah diurutkan menggunakan bubble sort: \n ");
                for (int i = 0; i < 1000; i++){
                    printf("%d ", data[i]);
                }
            } else if (array_choice == 2){
                int data[16000];
                for (int i = 0; i < 16000; i++){
                    data[i] = rand() % 10000;
                }
                bubble_sort(data, 16000);
                printf("Data setelah diurutkan menggunakan bubble sort: \n ");
                for (int i = 0; i < 16000; i++){
                    printf("%d ", data[i]);
                }
            } else if (array_choice == 3){
                int data[64000];
                for (int i = 0; i < 64000; i++){
                    data[i] = rand() % 10000;
                }
                bubble_sort(data, 64000);
                printf("Data setelah diurutkan menggunakan bubble sort: \n ");
                for (int i = 0; i < 64000; i++){
                    printf("%d ", data[i]);
                }
            } else {
                printf("Pilihan tidak valid.\n");
            }
        }
    }

    return 0;
}

int bubble_sort(int data[], int n){
    // bubble sort
    // mengurutkan data dengan cara membandingkan elemen bersebelahan dan menukarnya jika urutan salah

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

int selection_sort(int data[], int n){
    // selection sort
    // mengurutkan data dengan cara mencari elemen terkecil dan menukarnya dengan elemen pertama yang belum terurut

    for (int i = 0; i < n-1; i++){
        int min_idx = i;
        for (int j = i+1; j < n; j++){
            if (data[j] < data[min_idx]){
                min_idx = j;
            }
        }
        // swap
        int temp = data[i];
        data[i] = data[min_idx];
        data[min_idx] = temp;
    }
}

int linear_search(int target, int data[], int n){
    // linear search
    // mencari target dengan memeriksa setiap elemen dalam array satu per satu

    for (int i = 0; i < n; i++){
        if (data[i] == target){
            printf("Data %d ditemukan pada indeks %d menggunakan linear search.\n", target, i);
            return i;
        }
    }
    printf("Data %d tidak ditemukan menggunakan linear search.\n", target);
    return -1;
}

int binary_search(int target, int data[], int n){
    // binary search
    // mencari target dengan membagi array menjadi dua bagian dan menentukan bagian mana yang harus dicari lebih lanjut
    // syarat: array harus sudah terurut

    int left = 0;
    int right = n - 1;

    while (left <= right){
        int mid = left + (right - left) / 2;

        if (data[mid] == target){
            printf("Data %d ditemukan pada indeks ke-%d\n", target, mid);
            return mid;
        } else if (data[mid] < target){
            left = mid + 1; // cari di bagian kanan
        } else {
            right = mid - 1; // cari di bagian kiri
        }
    }
    printf("Data %d tidak ditemukan\n", target);
    return -1;
}

