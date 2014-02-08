#include <stdio.h>

typedef char tab[20];

struct student
{
    tab name;
    tab firstname;
    int age;
};

long makeMenu( void );
struct student addAStudent( void );
void showStudent( struct student myStudent );

int main( void )
{

    long choice;
    struct student myStudent;
    int defaultStudent;

    do
    {
        choice = makeMenu();
        switch (choice)
        {
             case 1:
                myStudent = addAStudent();
                showStudent( myStudent );
                break;
            case 2:
                showStudent( myStudent );
                break;
            default:
                printf ( "You choose %1d \n",choice );
                break;
        }
    }
    while ( choice != 4 );

    return(0);
}

struct student addAStudent( void )
{
    struct student myStudent;
    printf("Give the name \n");
    scanf("%s",&myStudent.name);
    printf("Give the lastname \n");
    scanf("%s",&myStudent.firstname);
    printf("Give the age \n ");
    scanf("%d",&myStudent.age);
    return (myStudent);
}

void showStudent( struct student myStudent )
{
    printf("Name \t\t = %s\n", myStudent.name );
    printf("Firstname \t = %s\n", myStudent.firstname);
    printf("Age \t\t = %d \n", myStudent.age);
    printf("\n");
}

long makeMenu ( void )
{
    long ret;
    printf ( "1. Edit the student\n" );
    printf ( "2. Show the student\n" );
    printf ( "4. Quit\n" );
    printf ( "Choose and type 1, 2, 3 or 4\n" );
    scanf ( "%1ld", &ret );
    fflush ( stdin ); /* fpurge for unix */
    return ret;
}

