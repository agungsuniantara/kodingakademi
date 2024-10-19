#include <stdio.h>

void main()
{
	char *s;
	int len,i;

	printf("\nENTER A STRING: ");
	gets(s); // fungsi gets mengambil karakter apapun dan mengubahnya ke string serta dapat menyimpan ke sebuah variabel

	len=strlen(s); // strlen fungsi menghitung panjang string

	printf("\nTHE REVERSE OF THE STRING IS:");

	for(i=len;i>=0;i--)
		printf("%c",*(s + i));

	getch();
}
