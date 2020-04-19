#include <stdio.h>

int main(){

    int m, n, i, num = 2;

    scanf("%d %d", &m, &n);

    for(int i=m; i<=n; i++){

        if(i == 1){
            continue;
        } else if(i == 2){
            printf("2\n");
            continue;
        }


        while(num != i){
            if(i % num == 0){
                num = -1;
                break;
            }
            num++;
        }

        if(num != -1)
            printf("%d\n", i);

        num = 2;

    }

    printf("\n");
    return 0;
}