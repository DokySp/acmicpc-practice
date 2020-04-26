#include <stdio.h>

int main(){

    int tc, h, w, n, i, j, N;

    scanf("%d", &tc);

    while(tc--){
        n = 0;
        scanf("%d %d %d", &h, &w, &N);  

        for(i=0; i<w; i++){
            for(j=0; j<h; j++){
                if(n == N-1){
                    printf("%d%02d\n", j+1, i+1);
                    n = -1;
                    break;
                } else {
                    n++;
                }
            }
            if(n == -1) break;
        }
    }

    return 0;
}