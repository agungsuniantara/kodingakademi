#include <stdio.h>
#include <stdbool.h>

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void swap(int* xp, int* yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n)
{
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = true;
            }
        }
        if (swapped == false)
            break;
    }
}

int partition(int arr[], int low, int high)
{
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

void quickSort(int arr[], int low, int high)
{
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int binarySearch(int array[], int x, int low, int high) {
  // Repeat until the pointers low and high meet each other
  while (low <= high) {
    int mid = low + (high - low) / 2;

    if (array[mid] == x)
      return mid;

    if (array[mid] < x)
      low = mid + 1;

    else
      high = mid - 1;
  }

  return -1;
}

void menu(){
    printf("1. Insertion Sort\n");
    printf("2. Bubble Sort\n");
    printf("3. QuickSort\n");
    printf("4. Sequential Search\n");
    printf("5. Binary Search\n");
    printf("0. Keluar \n");
}

int main(){
    int a,b;

    menu();

    printf("masukan pilihan : ");
    scanf("%d", &a);

    if (a == 1){
        printf("1. 1000 \n");
        printf("2. 16000 \n");
        printf("3. 64000 \n");
        printf("masukan pilihan : ");
        scanf("%d", &b);

        if (b == 1){
            a = 1000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%1000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
            printArray(array, n);
        }
        else if(b == 2){
            a = 16000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%16000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
            printArray(array, n);
        }
        else if(b == 3){
            a = 64000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%64000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            insertionSort(array, n);
            printArray(array, n);
        }
    }

    else if (a == 2){
        printf("1. 1000 \n");
        printf("2. 16000 \n");
        printf("3. 64000 \n");
        printf("masukan pilihan : ");
        scanf("%d", &b);

        if (b == 1){
            a = 1000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%1000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            bubbleSort(array, n);
            printArray(array, n);
        }
        else if(b == 2){
            a = 16000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%16000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            bubbleSort(array, n);
            printArray(array, n);
        }
        else if(b == 3){
            a = 64000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%64000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            bubbleSort(array, n);
            printArray(array, n);
        }
    }

    else if (a == 3){
        printf("1. 1000 \n");
        printf("2. 16000 \n");
        printf("3. 64000 \n");
        printf("masukan pilihan : ");
        scanf("%d", &b);

        if (b == 1){
            a = 1000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%1000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            quickSort(array, 0, n - 1);;
            printArray(array, n);
        }
        else if(b == 2){
            a = 16000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%16000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            quickSort(array, 0, n - 1);;
            printArray(array, n);
        }
        else if(b == 3){
            a = 64000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%64000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            quickSort(array, 0, n - 1);;
            printArray(array, n);
        }
    }

    else if (a == 4){
        printf("1. 1000 \n");
        printf("2. 16000 \n");
        printf("3. 64000 \n");
        printf("masukan pilihan : ");
        scanf("%d", &b);

        if (b == 1){
            a = 1000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%1000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            int d, ketemu, index_arr;

            printf("masukan angka : ");
            scanf("%d", &d);

            for(i=0;i<n;i++)
                {
                    if(d==array[i]){
                        ketemu = 1;
                        index_arr = i;
                    }
                }
            if(ketemu == 1){
                printf("\nangka %d ada pada index ke-%d",d,index_arr);
            }
            else{
                printf("\nangka %d tidak ada pada array",d);
            }
        }
        else if(b == 2){
            a = 16000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%16000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            int d, ketemu, index_arr;

            printf("masukan angka : ");
            scanf("%d", &d);

            for(i=0;i<n;i++)
                {
                    if(d==array[i]){
                        ketemu = 1;
                        index_arr = i;
                    }
                }
            if(ketemu == 1){
                printf("\nangka %d ada pada index ke-%d",d,index_arr);
            }
            else{
                printf("\nangka %d tidak ada pada array",d);
            }
        }
        else if(b == 3){
            a = 64000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%64000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            int d, ketemu, index_arr;

            printf("masukan angka : ");
            scanf("%d", &d);

            for(i=0;i<n;i++)
                {
                    if(d==array[i]){
                        ketemu = 1;
                        index_arr = i;
                    }
                }
            if(ketemu == 1){
                printf("\nangka %d ada pada index ke-%d",d,index_arr);
            }
            else{
                printf("\nangka %d tidak ada pada array",d);
            }
        }
    }

    else if (a == 5){
        printf("1. 1000 \n");
        printf("2. 16000 \n");
        printf("3. 64000 \n");
        printf("masukan pilihan : ");
        scanf("%d", &b);

        if (b == 1){
            a = 1000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%1000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            int d, ketemu, index_arr;

            printf("masukan angka : ");
            scanf("%d", &d);

            for(i=0;i<n;i++)
                {
                    if(d==array[i]){
                        ketemu = 1;
                        index_arr = i;
                    }
                }
            if(ketemu == 1){
                printf("\nangka %d ada pada index ke-%d",d,index_arr);
            }
            else{
                printf("\nangka %d tidak ada pada array",d);
            }

        }
        else if(b == 2){
            a = 16000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%16000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            int d, ketemu, index_arr;

            printf("masukan angka : ");
            scanf("%d", &d);

            for(i=0;i<n;i++)
                {
                    if(d==array[i]){
                        ketemu = 1;
                        index_arr = i;
                    }
                }
            if(ketemu == 1){
                printf("\nangka %d ada pada index ke-%d",d,index_arr);
            }
            else{
                printf("\nangka %d tidak ada pada array",d);
            }
        }
        else if(b == 3){
            a = 64000;
            int array[a],i;
            for(i=0;i<a;i++){
                array[i]=rand()%64000;
            }

            int n = sizeof(array) / sizeof(array[0]);

            int d, ketemu, index_arr;

            printf("masukan angka : ");
            scanf("%d", &d);

            for(i=0;i<n;i++)
                {
                    if(d==array[i]){
                        ketemu = 1;
                        index_arr = i;
                    }
                }
            if(ketemu == 1){
                printf("\nangka %d ada pada index ke-%d",d,index_arr);
            }
            else{
                printf("\nangka %d tidak ada pada array",d);
            }
        }
    }
}
