#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char a,b;
    printf("Type two chars, we will compare them : \n");
    printf("The first char = ");
    a = getchar();
    fflush(stdin);
    //fpurge(stdin);
    printf("The second char = ");
    b = getchar();
    printf("The comparision gives : \n");
    if ( a < b )
        {printf("'%c' is less than '%c'",a,b);}
    else if ( a > b )
        {printf("'%c' is greater than '%c' ",a,b);}
    else
        {printf("It's two times the same caracter!");}
    return(0);
}