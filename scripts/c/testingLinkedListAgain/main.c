#include <stdio.h>

struct person
{
    char *firstName;
    char *lastName;
    int age;
    struct person *next;
};

typedef struct person Person;

void showPerson ( Person *p  )
{
    if ( p !=0 )
        {
            printf ( "We store : %s, %s, %d at address %d\n", (*p).firstName, (*p).lastName,  (*p).age, p );
            showPerson ( (*p).next );
        }
}

Person addRecord ( void )
{
    Person p;
    p.next      = 0;
    p.firstName = malloc ( sizeof ( sizeof ( char ) * 20 ) );
    p.lastName  = malloc ( sizeof ( sizeof ( char ) * 20 ) );
    printf ( "Give the firstname, lastname and age of a person:\n" );
    scanf  ( "%s %s %d", p.firstName, p.lastName, &p.age );
    fflush ( stdin );
    showPerson ( &p );
    return p;
}

int main ( void )
{
    Person *begin;

    begin   = malloc ( sizeof ( Person ) ) ;
    *begin  = addRecord ();
    showPerson ( begin );
    printf ( "begin = %d , (*begin).next = %d\n", begin, (*begin).next );

    return ( 0 );
}