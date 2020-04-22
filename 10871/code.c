#include <stdio.h>

int main(){
    int N, X, a[10000], i;

    scanf("%d %d", &N, &X);
    for(i=0; i<N; i++)
        scanf("%d", &a[i]);

    for(i=0; i<N; i++)
        if(X>a[i]) printf("%d ", a[i]);

    printf("\n");

    return 0;
}