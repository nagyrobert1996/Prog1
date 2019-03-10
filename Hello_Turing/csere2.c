#include <stdio.h>

int main()
{
	int a = 0;
	int b = 0;
	printf("Adja meg az a szamot: ");
	scanf("%d" , &a );
	printf("Adja meg a b szamot: ");
	scanf("%d" , &b);
	b = b-a;
	a = a+b;
	b = a-b;
	printf("a=%d%s",a,"\n");
	printf("b=%d%s",b,"\n");

}