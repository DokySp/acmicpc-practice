#include <stdio.h>

int main(){
    int i, a, b, d;

    while(1){
        d = scanf("%d %d", &a, &b);
        // printf(":%d\n", d);  // Unix: Ctrl+D  / Win: Ctrl+Z  -> EOF!!
        if(d != EOF){
            printf("%d\n", a+b);
        } else {
            break;
        }
    }

    return 0;
}