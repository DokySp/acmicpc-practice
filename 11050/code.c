#include <stdio.h>

int main(){
    int n, k, ans = 1, i;

    scanf("%d %d", &n, &k);

    for(i=0; i<k; i++) ans *= n--;
    n = 1;
    for(i=1; i<=k; i++) n *= i;
    printf("%d\n", ans/n);

    return 0;
}