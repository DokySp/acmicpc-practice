// 14:41 .83

#include <stdio.h>
#include <stdlib.h>

int stack[30] = {0, };
int stackLength = 1;

int main(){

    int tc = 0;
    int i=0, j=0, T=0;
    int path[30][30] = {{0,},};
    int n, m = 0;

    scanf("%d", &tc);

    for(T=0; T<tc; T++) {

        scanf("%d", &n);
        scanf("%d", &m);

        for(i=0; i<n; i++){
            for(j=0; j<m; j++){
                path[i][j] = -1;
            }
        }

        



    }




    for(i=0; i<n; i++){
        for(j=0; j<m; j++){
            printf("%d ", path[i][j]);
        }
        printf("\n");
    }




    return 0;
}


int pop(){
    
    return 0;
}

void push(){

}