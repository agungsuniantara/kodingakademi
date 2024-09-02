#include <iostream>

using namespace std;

int main()
{
    int a;
    int* pc;
   
    a = 10;
    printf("alamat a = %p\n", &a);
    printf("value a = %d\n", a);

    pc = &a;
    printf("alamat pc = %p\n", &pc);
    printf("value pc = %d\n", *pc);

    *pc = 20;
    printf("alamat a = %p\n", &a);
    printf("value a = %d\n", a);
   
//    *pc = 2;
//    printf("Address of c: %p\n", &c);
//    printf("Value of c: %d\n\n", c); 
   return 0;

}
