#include <stdio.h>

#include <stdio.h>
#include <string.h>
struct Books
{
 char title[50];
 char author[50];
 char subject[100];
 int book_id;
};

void printBook( struct Books book );

int main( )
{
 struct Books Book1;
 struct Books Book2;

 strcpy( Book1.title, "My C Book");
 strcpy( Book1.author, "Anton K");
 strcpy( Book1.subject, "Tutorial V");
 Book1.book_id = 6495407;


 strcpy( Book2.title, "My D Book");
 strcpy( Book2.author, "Ali");
 strcpy( Book2.subject, "Tutorial D");
 Book2.book_id = 6495700;

 printBook( Book1 );
 printBook( Book2 );
 return 0;
}
void printBook( struct Books book )
{
 printf( "Book title : %s\n", book.title);
 printf( "Book author : %s\n", book.author);
 printf( "Book subject : %s\n", book.subject);
 printf( "Book book_id : %d\n", book.book_id);
}
