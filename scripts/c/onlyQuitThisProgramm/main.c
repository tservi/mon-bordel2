#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char c = ' ';
    while ( c != 'q' && c != 'Q' )
    {
        fflush(stdin); /* will be fpurge(stdin) in Unix */
        printf("Please leave this programm by typing the q key and enter ");
        c = getchar();
    }
}