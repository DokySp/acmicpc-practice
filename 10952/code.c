#include <stdio.h>

int main(){

    int a, b, i;

    while(1){
        scanf("%d %d", &a, &b);
        if(a==0 && b==0) break;
        printf("%d\n", a+b);
    }
    return 0;
}