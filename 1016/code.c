#include <stdio.h>
#include <stdlib.h>

// 01:37:00

int main(){
    long min, max, i, j, count = 0;
    scanf("%ld %ld", &min, &max);

    char *a = (char*)malloc(sizeof(char)*(max-min+1));
    // printf("\n%ld\n", max-min+1);
    // 1000000000000 1000001000000 : 최대
    // 999000000 1000000000 : 좀 걸림
    // 9999000000 10000000000 : 오래걸림..

    for(i=2; i<=max; i++){
        for(j=(min/(i*i)); i*i*j<=max; j++){

            // i*i*j 값이 범위 안에 있을 시
                // 해당하는 배열에 표시 
            if(i*i*j >= min){
                *(a+(i*i*j)-min) = 1;
            }
        }
    }

    for(i=0; i<=max-min; i++){
        if(*(a+i) == 0) count++;
    }

    printf("\n%ld\n", count);

    free(a);
    return 0;
}

