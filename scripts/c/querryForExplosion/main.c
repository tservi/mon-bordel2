#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int ret = 0;
    char c;
    printf("Hello\n");
    printf("Press Y or y to make your computer explode : \n");
    c = getchar();
    fflush(stdin);
    if ( c == 'Y' || c == 'y' )
    {
        printf("Booooooum !\n");
        ret = 1;
    }
    else
        {printf("Goodbye!\n");}
    return(ret);
}