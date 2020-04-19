#include <stdio.h>

int main(){
    int i, max=-1000001, min=1000001, inp, tc;

    scanf("%d", &tc);

    for(i=0; i<tc; i++){
        scanf("%d", &inp);
        if(max < inp)
            max = inp;
        if(min > inp)
            min = inp;
    }

    printf("%d %d\n", min, max);

    return 0;
}