#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int start;
    char entry[20];
    do
    {
        printf("Give a starting point : \n");
        scanf("%s", entry);
        start = atoi (entry);
    }
    while ( start < 0 || start > 20);
    do
    {
        printf("%d \n",start);
        start--;
    }
    while(start>=0);
    return(0);
}