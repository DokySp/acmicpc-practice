#include <stdio.h>

int main(){

    int inp[2] = {0, };
    int i, tmp;

    scanf("%d %d", &inp[0], &inp[1]);

    for(i=0; i<2; i++){
        tmp = 0;
        tmp += inp[i]/100; // 100자리 -> 1자리
        tmp += ((inp[i]/10) % 10) * 10;
        tmp += (inp[i] % 10) * 100;
        inp[i] = tmp;
    }

    printf("%d\n", inp[0] > inp[1] ? inp[0] : inp[1]);

    return 0;
}