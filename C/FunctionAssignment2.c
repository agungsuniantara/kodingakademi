#include<stdio.h>

int factorial(int n)
{
  if (n == 0)
    return 1;
  else
    return(n * factorial(n-1));// 5 * 4 * 3 * 2 * 1
}

void main()
{
  int number;
  int fact;
  printf("Enter a number: ");
  scanf("%d", &number);

  fact = factorial(number);
  printf("Factorial of %d is %d\n", number, fact);
}

