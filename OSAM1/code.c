#include <stdio.h>

int main(){

    int tc = 12;
    int inp = 0;
    int max = -10, min = 110;
    int avg = 0;

    while(tc--) {
        scanf("%d", &inp);
        if(min > inp) min = inp;
        if(max < inp) max = inp;
        avg += inp;
    }

    printf("%.1lf\n", (float)(avg-(min+max))/10 );

    return 0;
}