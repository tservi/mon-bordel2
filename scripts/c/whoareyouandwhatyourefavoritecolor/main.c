#include <stdio.h>
#include <stdlib.h>

int main()
{
    char name[20];
    char color[20];
    printf("Hello world!\n");
    printf("Who are you : \n");
    gets(name);
    printf("What your favorite color : \n");
    gets(color);
    printf("Well, your name is %s and your favorite color is %s",name,color);
    return 0;
}
