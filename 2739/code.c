#include <stdio.h>

int main(){
    int i, lev;

    scanf("%d", &lev);

    for(i=1; i<=9; i++){
        printf("%d * %d = %d\n", lev, i, lev*i);
    }

    return 0;
}