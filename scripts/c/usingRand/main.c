#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define LOOP 10

int main()
{
    int index;
    srand((unsigned)time(NULL));
    printf("Hello world!\n");
    printf("RAND_MAX is equal to %u\n",RAND_MAX);
    for ( index = 0; index < LOOP ; index++ )
        {printf("%d\n",rand());}
    printf("RAND_MAX is equal to %u\n",RAND_MAX);
    return 0;
}
