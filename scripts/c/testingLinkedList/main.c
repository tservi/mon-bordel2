#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//typedef struct person person;

struct person
{
    char firstname[20];
    char name[20];
    struct person *next;
};

void menu ( void )
    { printf ( "Please give an order : \na for add \nl for list \nq for quit \nm for menu \n" ); }

void showList ( struct person *p )
{
    struct person cursor;
    if ( p != 0 )
    {
        cursor = *p;
        printf ( "We store firstname = %s, name = %s at the address : %d \n", cursor.firstname , cursor.name , p );
        if ( cursor.next != 0 )
            { showList ( cursor.next ); }
    }
}

struct person newPerson ( void )
{
    struct person np;
    np.next = 0;
    printf ( "Give a lastname and a name to store :\n");
    scanf ( "%s %s", &np.firstname, &np.name );
    fflush ( stdin );
    return np;
}


int main ( void )
{
    struct person *begin = 0;
    struct person *nPers; // = malloc ( sizeof ( struct person ) );
    char order;
    menu ();
    do
    {
        printf ( "Your order : " );
        scanf ( "%c", &order );
        fflush ( stdin );
        switch ( order )
        {
            case 'a':
                nPers = malloc ( sizeof ( struct person ) );
                *nPers = newPerson ();
                if ( begin == 0 )
                    {   begin = nPers; }
                else
                    {
                        struct person *cursor;
                        cursor = begin;
                        while ( (*cursor).next != 0 )  // could be "while ( cursor -> next )" too!
                                {cursor = (*cursor).next; }
                        (*cursor).next = nPers;
                    }
                break;
            case 'l':
                if ( begin == 0)
                    { printf ( "Nobody in database! \n"); }
                else
                {
                    printf ( "Listing all persons : \n");
                    showList ( begin );
                }
                break;
            case 'm':
                menu ();
                break;
            case 'q':
                printf ( "See you soon ...\n" );
                break;
            default:
                printf ( "I do not understand %c \n", order );
                break;
        };

    }
    while ( order != 'q' );

    return ( 0 );
}