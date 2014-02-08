#include <stdio.h>

int main(void)
{

    int  a, b;
    int *c;
    int *d;
    a = 10;
    printf("valeur de a = %d \n",a);
    printf("adresse de a = &a = %d \n",&a);
    printf("---------------------------------------------------------------\n\n");

    b = 20;
    printf("valeur de b = %d \n",b);
    printf("adresse de b = &b = %d \n",&b);
    printf("---------------------------------------------------------------\n\n");

    c = &a;
    printf("valeur de c = %d \n",c);
    printf("valeur pointee par c = *c = %d \n",*c);
    printf("adresse de c = &c = %d \n",&c);
    printf("---------------------------------------------------------------\n\n");

    b = *c + 100;
    printf("valeur de b = %d \n",b);
    printf("adresse de b = &b = %d \n",&b);
    printf("---------------------------------------------------------------\n\n");

    *c = *c + 200 ;
    printf("valeur de a = %d \n",a);
    printf("adresse de a = &a = %d \n",&a);
    printf("---------------------------------------------------------------\n\n");

    (*c)++;
    printf("valeur de a = %d \n",a);
    printf("adresse de a = &a = %d \n",&a);
    printf("---------------------------------------------------------------\n\n");

    c = &a;
    d = &b;
    printf("valeur de a = %d\n",a);
    printf("adresse de a = &a = %d  =? c = %d \n",&a,c);
    printf("valeur de b = %d \n",b);
    printf("adresse de b = &b = %d  =? d = %d \n",&b,d);
    printf("---------------------------------------------------------------\n\n");;

    *c = (*d)++;
    printf("valeur de a = %d\n",a);
    printf("adresse de a = &a = %d  =? c = %d \n",&a,c);
    printf("valeur de b = %d \n",b);
    printf("adresse de b = &b = %d  =? d = %d \n",&b,d);
    printf("---------------------------------------------------------------\n\n");;

    *c *= *d; // le contenu pointé par c est multiplié par le contenu pointé par d ==> a *= b; ==> a = a * b;
    printf("valeur de a = %d \n", a );
    printf("adresse de a = &a = %d  =? c = %d \n",&a,c);
    printf("valeur de b = %d \n",b);
    printf("adresse de b = &b = %d  =? d = %d \n",&b,d);
    printf("---------------------------------------------------------------\n\n");;




}