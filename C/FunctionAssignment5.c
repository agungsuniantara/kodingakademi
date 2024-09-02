 #include<stdio.h>
int Fibonacci(int n){
    static int n1=0,n2=1,n3;
    if(n>0){
        Fibonacci(n-1);
         n3 = n1 + n2;
         n1 = n2;
         n2 = n3;
    }
    return n3;
}
int main(){
    int n;
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    printf("Fibonacci Series: ");
    int hasil = Fibonacci(n);
    printf("angka terakhir = %d", hasil);
  return 0;
 }
