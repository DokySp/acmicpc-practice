#include <stdio.h>
#include <stdlib.h>

long long comb(int, int);

int main(){
    int tc = 0;
    int n, m, T = 0;
    scanf("%d", &tc);

    for(T=0; T<tc; T++) {
        scanf("%d", &n);
        scanf("%d", &m);
        printf("%lld\n", comb(m,n));
    }
    return 0;
}


long long comb(int n, int r){
    long long res = 1;
    long long tmp = 1;
    int i = 0;

    if(n/2 < r)
        r = n - r;
    
    for(i=n; i>= n-(r-1); i--)
        res *= i;
    for(i=r; i > 0; i--)
        tmp *= i;
    printf("%lld %lld\n", res, tmp);
    return res/tmp;
}