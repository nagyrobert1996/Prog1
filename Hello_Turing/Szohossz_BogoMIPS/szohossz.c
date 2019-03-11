#include <stdio.h>
int main()
{
	int a=1;
	int n=1;
	while(a<<=1)
	{
		n+=1;
	}
	printf("Megoldas:%d%s",n,"\n");
}
