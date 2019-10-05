#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,i,sum=0;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    for(i = 0; i<5;i++){
        sum+=n%10;
        n/=10;
    }
    printf("%d",sum);
    return 0;
}

