#include <stdio.h>

// 25

int main(){

    int n, m, card[100], sort[100], i, max, si = 0, maxi = 0, k, ansCount = 0, ans = 0;

    scanf("%d %d", &n, &m);
    

    for(i=0; i<n; i++)
        scanf("%d", &card[i]);
    
    for(k=0; k<n; k++){
        for(i=0; i<n; i++){
            if(card[i] > max){
                max = card[i];
                maxi = i;
            }
        }
        sort[si] = card[maxi];
        card[maxi] = -1;
        si++;
        max = -1;
    }

    


    for(i=0; i<n; i++){
        if(ans+sort[i] <= m){
            printf("a: %d\n", sort[i]);
            ans += sort[i];
            ansCount++;
        }

        if(ansCount == 3){
            break;
        }

    }


    printf("%d\n", ans);


    return 0;
}



