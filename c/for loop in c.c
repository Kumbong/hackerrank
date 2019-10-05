#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    char *num_words[10] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    int i ;

    for(i=a;i<=b;i++){
        if(i<=9){
            printf("%s\n",num_words[i]);
        }
        else{
            if(i%2==0)
                printf("even\n");
            else
                printf("odd\n");
        }
    }
    return 0;
}

