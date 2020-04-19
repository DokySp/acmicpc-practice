#include <stdio.h>

int main(){
    int max = 0, maxI;
    int inp;
    int i;

    for(i=0; i<9; i++){
        scanf("%d", &inp);
        if(max < inp){
            max = inp;
            maxI = i;
        }
    }

    printf("%d\n%d\n", max, maxI+1);

    return 0;
}