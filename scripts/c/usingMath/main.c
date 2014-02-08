#include <stdio.h>
#include <math.h>

int main()
{
    double test = 4.0;
    double power = 0.5 ;
    printf("Hello world!\n");
    printf("%.0f ^ %.2f = %.0f",test,power,pow(test,power));
    return 0;
}
