
#include <stdio.h>
#include <string.h>

void reverseString(char *str) {
    char *ptr1 = str;  // Pointer to the first character
    char *ptr2 = str + strlen(str) - 1;  // Pointer to the last character

    while (ptr1 < ptr2) {
        // Swap characters pointed by ptr1 and ptr2
        char temp = *ptr1;
        *ptr1 = *ptr2;
        *ptr2 = temp;

        // Move pointers towards each other
        ptr1++;
        ptr2--;
    }
}

int main() {
    char input[100];

    printf("Enter a string: ");
    scanf("%s", input);

    reverseString(input);

    printf("Reversed string: %s\n", input);

    return 0;
}
