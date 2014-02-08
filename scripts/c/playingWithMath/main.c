#include <stdio.h>

#define UneConstante 69.0

int main()
{
/*
    char name[300];
    printf("Hello world!\n");
    printf("Hello, what's you're name?\n");
    gets(name);
    printf("Nice to meet you %s \n",name);

    int age = 999;
    printf("Mathusaleh war %d age old\n\n",age);

    char entry[20];
    int entryage;
    printf("How hold was Matusaleh?\n");
    gets(entry);
    entryage = atoi( entry );
    printf("So you think he was %d years old.\n\n",entryage);
*/
    char entry[20];
    char test[] = "Hello cruel world";
    printf("%s %.2f \n", test, UneConstante);
    double a, b, c = 0.0;
    printf("Calculing c = sqrt( a*a + b*b )  \n");
    printf("How long is a in a triangle : ");
    gets(entry);
    a = atoi(entry);
    printf("You're entry : %.2f \n",a);
    printf("How long is a in b triangle : ");
    gets(entry);
    b = atoi(entry);
    printf("You're entry : %.2f \n",b);
    c = a*a + b*b;
    printf(" c * c = %.2f\n ",c);

    char ch;
    ch = getchar();
    printf("You type : %c \n",ch);
    printf("The ASCII value is : %d \n",ch);

    return 0;
}
