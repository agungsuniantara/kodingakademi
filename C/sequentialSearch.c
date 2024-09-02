#include<stdio.h>

int main() {
 int i;
 int Array[ ] = {50,12,13,15, 4,40 ,60, 30,85,40};
 int key ; // key is number to be searched
 int Size = sizeof(Array) / sizeof(int);
 printf("Enter the number to be searched:");
 scanf("%d", &key);
 for( i =0; i< Size; i++)
  if( Array[i]== key)  {
    printf("Yes, it is in Array. Array[%d]=%d\n", i, Array[i]);
    goto End;
  }
  printf("The number is not in Array.\n");
  End:
  return 0;
}
