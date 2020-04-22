#include <stdio.h>

int main(){

    int a, inp = 5, sum = 0;

    while(inp--){
        scanf("%d", &a);
        a %= 10;
        sum += a*a;
    }
    
    printf("%d\n", sum%10);

    return 0;
}