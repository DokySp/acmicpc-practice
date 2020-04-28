#include <stdio.h>

int main(){

    int inp[1000000] = {0, };
    int min = 1000001;
    int num, i, j, trig;

    scanf("%d", &num);

    for(i=0; i<num; i++) scanf("%d", &inp[i]);

    for(i=0; i<num; i++){
        for(j=0; j<num; j++){
            if(min > inp[j]){
                min = inp[j];
                trig = j;
            }
        }

        printf("%d\n", inp[trig]);
        min = 1000001;
        inp[trig] = 1000001;

    }


    return 0;
}