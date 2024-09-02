#include <stdio.h>
#include <stdlib.h>

int main()
{
    int inputNum;
    printf("Input number: ");
    scanf("%d", &inputNum);
    showNumber(inputNum);
}

int showNumber(int number){
    int result;
    if(number!=0)
        result=showNumber(number-1);
    printf("%d  ", result);
    return result+1;
}
