#include <stdio.h>
#include <math.h>

void update(int *a,int *b) {
    // Complete this function  
    int temp_a = *a;  
    int temp_b = *b;
    *a = temp_a + temp_b;
    *b = abs(temp_a - temp_b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

