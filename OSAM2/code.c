#include <stdio.h>

int main(){

    int tc = 0;
    int i = 0;
    int inp = 0;
    int m[100000] = {0, };

    scanf("%d", &tc);

    for(i=0; i<tc; i++){
        scanf("%d", &inp);
        m[inp]++;
    }

    for(i=0; i<100000; i++){
        if(m[i] == 1) printf("%d\n", i);
    }




    return 0;
}