#include <stdio.h>

int main()
{
    float celsius, fahrenheit;

    printf("Enter temperature in Fahrenheit: ");
    scanf("%f", &fahrenheit);

    celsius = (fahrenheit - 32) * 5 / 9;

    printf("%.2f Fahrenheit = %.2f Celsius", fahrenheit, celsius);

    if(celsius >= 18 && celsius <= 24){
        printf("\nideal temperature");
    }
    else if(celsius <= 18){
        printf("\nlow temperature");
    }
    else{
        printf("\nhigh temperature");
    }

    return 0;
}
