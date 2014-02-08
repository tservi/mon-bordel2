#include <stdio.h>

int main(void)
{
    char wDays[][10] = { "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"};
    int len = sizeof ( wDays ) / sizeof ( wDays[0] );
    int i ;
    for ( i = 0; i < len ; i++ )
        { wDays[i][0] = toupper ( wDays[i][0] ); }
    for ( i = 0; i < len ; i++ )
        { printf ( "%d = %d = %10s = len : %d \n", i , &wDays[i] , wDays[i] , strlen ( wDays[i] )  ); }
    puts ( "---------------------------------------------------------------");


    char *days[] = { "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"};
    len = sizeof ( days ) / sizeof ( days[0] );
    for ( i = 0; i < len ; i++ )
    {
        //printf ( "%c %d - ", toupper ( *( days[i]+0 ) ), strlen( days[i] ) );
        int lenDay = strlen ( days[i] );
        char newString[ lenDay+1 ];
        newString[0] = toupper ( *( days[i] ) );
        int j;
        for ( j = 1 ; j < lenDay ; j++ )
            { newString[j] = *( days[i] + j ); }
        newString[lenDay] = '\0';
        printf ( "'%s' %d / ", newString, &newString );
    }
    puts ( "\n" );
    for ( i = 0; i < len ; i++ )
        { printf ( "%d = %d = %10s = len : %d \n", i , &days[i] , days[i] , strlen ( days[i] )  ); }

    return ( 0 );

}