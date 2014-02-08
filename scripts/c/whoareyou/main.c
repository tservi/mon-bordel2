#include <stdio.h>
#include <stdlib.h>

int main()
{
    char me[20];
    printf("Hello world!\n");
    printf("%15s","right\n");
    printf("%-15s","left\n");
    printf("What's you're name : \n");
    scanf("%s",&me);
    printf("Glad to see you : %s \n",me);
    return 0;
}
