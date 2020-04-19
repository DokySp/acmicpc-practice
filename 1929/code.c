#include <stdio.h>

int main(){

    int m, n, i, num;
    int pn[1000000] = {-1, -1, 0, 0, -1, 0, };

    scanf("%d %d", &m, &n);

    for(i=2; i<1000000; i++){ // 1000000을 루트 N으로 고쳐도 된다!
        if(pn[i] == -1)
            continue;

        for(num = i*2; num < 1000000; num += i){  // i*2 !! 본인은 제외
            pn[num] = -1;
        }

    }

    for(i=m; i<=n; i++){
        if(pn[i] == 0)
            printf("%d ", i);
    }

    printf("\n");
    return 0;
}