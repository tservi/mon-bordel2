#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{

    char string[] = "hello world!";
    puts( string );
    string[0] = 'H' ;
    //int len = sizeof ( string ) - 1 ;
    int len = strlen ( string );
    printf ( "len of '%s' = %d \n", string, len );
    char *begin, *offset;
    begin = string ;
    for ( offset = string ; offset - begin < len ; offset++ )
        { printf ( "%c \n", *offset ) ; }
    for ( offset = &string[len-1] ; offset >= begin ; offset-- )
        { printf ( "%c", *offset ) ; }
    puts ( "" );
    printf("---------------------------------\n\n");
    int *c;
    for ( offset = string ; offset - begin < len ; offset++ )
        { printf ( "%c", toupper ( *offset ) ) ; }
    puts ( "" );

    printf("---------------------------------\n\n");
    char *newString;
    strcpy ( newString, "Hello world by t-servi.com !" );
    printf ( "%s \n", newString );
    strcpy ( newString, "Hello world by t-servi.com , bis!" );
    printf ( "%s \n", newString );
    strcpy ( newString, "Hello world by t-servi.com , tierce!" );
    printf ( "%s \n", newString );

    printf("---------------------------------\n\n");
    char s1[20], s2[20], s3[20], s4[20], s5[20] ;
    puts ( "Give 5 strings");
    scanf ( "%s %s %s %s %s", &s1, &s2, &s3, &s4, &s5);
    printf ( "Inversion = %s %s %s %s %s \n", s5, s4, s3, s2, s1 );

    return ( 0 );
}