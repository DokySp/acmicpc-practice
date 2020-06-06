#include <stdio.h>

int main(){

    int tc = 0;
    int i, j;

    int aLen = 0, mLen = 0;
    int A[100000] = {0, };
    int M[100000] = {0, };

    scanf("%d", &tc);
    for(i=0; i<tc; i++)
        scanf("%d", &A[i]);
    aLen = tc;

    scanf("%d", &tc);
    for(i=0; i<tc; i++)
        scanf("%d", &M[i]);
    mLen = tc;

    for(i=0; i<mLen; i++){
        for(j=0; j<aLen; j++){
            if(M[i] == A[j]){
                printf("1\n");
                break;
            }
        }
        if(aLen == j) printf("0\n");
    }

    return 0;
}

