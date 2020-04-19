#include <stdio.h>

int main(){

    int tc, a, b, i;

    scanf("%d", &tc);

    for(i=0; i<tc; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }

    return 0;
}