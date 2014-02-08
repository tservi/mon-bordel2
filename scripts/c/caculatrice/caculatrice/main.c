#include <curses.h>
#include <string.h>

int main()
{
    /* declaration */
    int c;                          /* caractere rentre a l'ecran */
    int operation;                  /* l'operation a effectuer */
    double nombreEnEntree;          /* le nombre actuellement en construction */
    double nombreStocke;            /* le nombre resultant de l'operation */
    int decimal;                    /* le drapeau pour une valeur decimale */
    /* initialisation */
    operation=0;
    nombreEnEntree=0;
    nombreStocke=0;
    decimal=0;
    /* debut du programme */
    initscr();
	raw();
	noecho();
	printw("Bienvenue dans la calculatrice!\nAppuyez sur q ou sur Q pour quitter!\nAppuyez sur a ou A pour l\'aide\n");
	refresh();
    do
        {
            c=getch();
            if(c>='0' && c<='9')
                {
                    printw("%c",c);
                    nombreEnEntree=(c-48.0)+10.0*(double)nombreEnEntree; /* en ASCII le zero commence a 48 */
                    printw(" %d %d ",c-48, nombreEnEntree);
                }:
            if (c=='+' || c=='-' || c=='*' || c=='/' ||  c=='%')
                {
                    printw(" %c \n",operation);
                    if(operation!=0)
                        {printw("%d ",nombreEnEntree+nombreStocke);}
                    nombreStocke=nombreEnEntree;
                    nombreEnEntree=0;
                    operation=c;
                }
            if (tolower(c)=='m')
                {
                    clear();
                    operation=0;
                    nombreEnEntree=0;
                    nombreStocke=0;
                    decimal=0;
                }
            if (tolower(c)=='a')
                {
                    clear();
                    printw("Operations :\n+ => addition\n- => soustraction\n* => multiplication\n/ => division\n% => modulo\nm => mettre a zero et effacer l\'ecran\na => aide\nq => quitter\n");
                }
        }
    while(tolower(c)!='q');
	endwin();
	return 0;
}

