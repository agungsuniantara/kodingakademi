#include <stdio.h>

void insertionSort(int array[], int size) {
  for (int step = 1; step < size; step++) {
    int key = array[step];
    int j = step - 1;

    while (key < array[j] && j >= 0) {
      array[j + 1] = array[j];
      --j;
    }
    array[j + 1] = key;
  }
}

void bubbleSort(int array[], int size) {

  // loop to access each array element
  for (int step = 0; step < size - 1; ++step) {

    // loop to compare array elements
    for (int i = 0; i < size - step - 1; ++i) {

      // compare two adjacent elements
      // change > to < to sort in descending order
      if (array[i] > array[i + 1]) {

        // swapping occurs if elements
        // are not in the intended order
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// function to find the partition position
int partition(int array[], int low, int high) {

  // select the rightmost element as pivot
  int pivot = array[high];

  // pointer for greater element
  int i = (low - 1);

  // traverse each element of the array
  // compare them with the pivot
  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {

      // if element smaller than pivot is found
      // swap it with the greater element pointed by i
      i++;

      // swap element at i with element at j
      swap(&array[i], &array[j]);
    }
  }

  // swap the pivot element with the greater element at i
  swap(&array[i + 1], &array[high]);

  // return the partition point
  return (i + 1);
}

void quickSort(int array[], int low, int high) {
  if (low < high) {

    // find the pivot element such that
    // elements smaller than pivot are on left of pivot
    // elements greater than pivot are on right of pivot
    int pi = partition(array, low, high);

    // recursive call on the left of pivot
    quickSort(array, low, pi - 1);

    // recursive call on the right of pivot
    quickSort(array, pi + 1, high);
  }
}

// function to print array elements
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
  printf("\n");
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
  return 0;
}

int main(){
    printf("PROGRAM PENGURUTAN DAN PENCARIAN \n\n");

    printf("Urutkan array berikut ini {9, 5, 1, 4, 3} \n\n");

    printf("1. Insertion sort \n");
    printf("2. Bubble sort \n");
    printf("3. Quick sort \n");
    printf("4. Sequential search \n");
    printf("5. Binary search \n");
    printf("0. keluar \n\n");

    int data[] = {9, 5, 1, 4, 3};
    int size = sizeof(data) / sizeof(data[0]);
    int key;
    int hasil;
    int kunci;

    int pilih;
    printf("pilih nomer : ");
    scanf("%i", &pilih);

    switch(pilih){
    case 1:
        insertionSort(data, size);
        printf("Sorted array in ascending order:\n");
        for (int i = 0; i < size; i++) {
            printf("%d ", data[i]);
        }
            printf("\n");
        break;

    case 2:
        bubbleSort(data, size);
        printf("Sorted array in ascending order:\n");
        for (int i = 0; i < size; i++) {
            printf("%d ", data[i]);
        }
            printf("\n");
        break;

    case 3:
        quickSort(data, 0, size - 1);
        printf("Sorted array in ascending order: \n");
        printArray(data, size);
        break;

    case 4:
        printf("Enter the number to be searched : ");
        scanf("%d", &key);

        for(int i = 0; i < size; i++){
            if(data[i] == key){
                printf("angka %d ada pada index array yang ke %d", key, i);
            }
        }
        break;

    case 5:
        printf("Enter the number to be searched : ");
        scanf("%d", &kunci);

        hasil = binarySearch(data, kunci, 0, size - 1);

        printf("angka ditemukan pada index ke %d", hasil);

        break;

    case 0:
        printf("sistem keluar !");
        break;
    }
}


