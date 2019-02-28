#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void jelkezelo ()
{
	printf("Vegtelen ciklus");
	printf("\n");
}

int main()
{
	for(;;)
	{
		if (signal (SIGINT, jelkezelo) == SIG_IGN)
			signal (SIGINT, SIG_IGN);
	}
	return 0;
}
