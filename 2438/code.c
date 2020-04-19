#include <stdio.h>

int main(){

    int lev = 0;
    int i, j;
    scanf("%d", &lev);

    for(i=0; i<lev; i++){
        for(j=0; j<=i; j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}