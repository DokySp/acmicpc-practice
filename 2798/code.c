#include <stdio.h>

int main(){

    int n, m, card[100], ans, a, b, c, c1, c2, c3, max = -1;

    scanf("%d %d", &n, &m);

    for(a=0; a<n; a++)
        scanf("%d", &card[a]);

    for(a=0; a<n-2; a++){
        for(b=a+1; b<n-1; b++){
            for(c=b+1; c<n; c++){
                if( card[a]+card[b]+card[c] <= m && card[a]+card[b]+card[c] > max){
                    max = card[a]+card[b]+card[c];
                }
            }
        }
    }

    printf("%d\n", max);


    return 0;
}



