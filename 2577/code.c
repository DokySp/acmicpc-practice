#include <stdio.h>

int main(){

    int input = 0;
    int res = 1, i;
    int count[10] = {0, };

    for(i=0; i<3; i++){
        scanf("%d", &input);
        res *= input;
    }
    
    while(res != 0){
        count[res % 10]++;
        res = res / 10;
    }

    for(i=0; i<10; i++){
        printf("%d\n", count[i]);
    }

    return 0;
}