#include <stdio.h>


int main(void)
{
    int test = 64;
    double test2 = 256.256;
    printf("%d * 2 = %d \n", test, test << 1 );
    printf("%d * 4 = %d \n", test, test << 2 );
    printf("%d * 8 = %d \n", test, test << 3 );
    printf("%d / 2 = %d \n", test, test >> 1 );
    printf("%d / 4 = %d \n", test, test >> 2 );
    printf("%d / 8 = %d \n", test, test >> 3 );
    printf("%d * 2 = %d \n", (int)test2, (int)test2 << 1 );
}