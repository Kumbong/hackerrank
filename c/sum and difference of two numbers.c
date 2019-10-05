#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int n,m;
    float a,b;

    scanf("%d %d",&n,&m);
    printf("%d %d\n",n+m,n-m);
    scanf("%f %f",&a,&b);
    printf("%0.1f %0.1f",a+b,a-b);
    
    return 0;
}

