#include <stdio.h>

int main(){
    int a, b, big, gcd = 1, i;
    scanf("%d %d", &a, &b);

    big = a > b ? a : b;

    while(1){
        for(i = 2; i <= big; i++){
            if(a%i == 0 && b%i == 0){
                a /= i;
                b /= i;
                gcd *= i;
                break;
            }
        }
        if(big == i-1 || a == 1 || b == 1) break;
    }

    printf("%d %d\n", gcd, gcd * a * b);

    return 0;
}