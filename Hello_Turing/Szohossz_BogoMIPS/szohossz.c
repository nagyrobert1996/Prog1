#include <stdio.h>
int main()
{
	int a=1;
	int n=0;
	while(a!=0)
	{
		n+=1;
		a=a<<1;
	}
	printf("Megoldas:%d%s",n,"\n");
}
