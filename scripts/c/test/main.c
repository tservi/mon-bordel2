/*
voir : http://c-faq.com/osdep/cbreak.html depuis http://en.wikipedia.org/wiki/Conio.h

solution pour windows

#include <stdio.h>
#include <conio.h>

int main()
{
    int c;
    puts("Welcome. \nPress Q or q to quit! ");
    do
    {c=getch();}
    while (c!=EOF && c!='\n' && c!='Q' && c!='q');
    return 0;

}

autre possibilite : utilisation de ncurses implémenté pour linux et pour windows ...
http://pdcurses.slashon.com/

*/

#include <curses.h>

int main()
{
    char c;
	initscr();			/* Start curses mode 		  */
	cbreak();
	noecho();
	printw("Welcome!\nPress q or Q to quit!\n");	/* Print Hello World		  */
	refresh();			/* Print it on to the real screen */
	do
        {c=getch();			/* Wait for user input */}
    while(tolower(c)!='q');
	endwin();			/* End curses mode		  */

	return 0;
}

