#include <stdio.h>

void bomb(int times);
void descend(void);

int main(void)
{
    printf("Welcome to bombing test zone!\n");
    bomb(15);
    return(0);
}

void bomb(int times)
{
    int i = 0;
    for ( i = 0; i < times ; i++)
    {
       descend();
    }
    printf(" BOUM! \n");
}

void descend(void)
{ printf("   *    \n");}