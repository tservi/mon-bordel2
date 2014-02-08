#include <stdio.h>

int main(void)
{
    int notes[][5] = { { 6, 6, 6, 6, 6 } , { 4, 4, 4, 4, 4 } , { 5, 3, 5, 3, 5 } , { 2, 2, 2, 2 } };

    int nbStudents = sizeof ( notes ) / sizeof ( notes [0] ) ;
    int nbNotes =  sizeof ( notes [0] ) / sizeof ( notes [0][0] ) ;
    //printf ( "%d \n", nbStudents )  ;
    //printf ( "%d \n", nbNotes )  ;

    int *n;

    float middle[nbStudents];
    n = notes;
    int i, j;
    for ( i = 0; i < nbStudents; i++)
    {
        int total = 0;
        for ( j = 0; j < nbNotes; j++ )
        {
            total += *( *( notes+i ) + j ); // ==> notes[i][j]
        }
        *( middle + i ) = (float)total / (float)nbNotes; // ==> middle[i] = (float)total / (float)nbNotes;
    }
    for ( i = 0; i < nbStudents; i++)
    {
        float show = *( middle + i ); // ==> middle[i]
        long address = middle+i; // ==> &middle[i]
        printf ( "%d = %.2f , address = %d \n", i, show, address  );
    }
    long lastAddress = middle + --i;
    printf ( "last address = %d \n", lastAddress );
    printf ( "first note = %.2f \n", *( middle ) );
    printf ( "--------------------------------------------------\n" );

    float *begin, *offset;
    begin = middle;
    printf ( "first note = %.2f \n", begin );
    for ( offset = middle ; offset - begin < (float)nbStudents ; offset++)
    {
        printf ( "student %d: note = %.2f \n", (int)(offset - begin)+1, *offset );

    }

    printf ( "--------------------------------------------------\n" );
    int A[] = {12, 23, 34, 45, 56, 67, 78, 89, 90};
    int *P;
    P = A;
    printf ( "%d \n", *P+2 ) ;
    printf ( "%d \n", *(P+2) ) ;
    printf ( "%d \n", &P+1 ) ;
    printf ( "%d \n", &A[4]-3 ) ;
    printf ( "%d \n", A+3 ) ;
    printf ( "%d \n", &A[7]-P ) ;
    printf ( "%d \n", P+(*P-10) ) ;
    printf ( "%d \n", *(P+*(P+8)-A[7]) ) ;

}