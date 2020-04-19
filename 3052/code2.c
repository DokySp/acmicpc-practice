#include <stdio.h>

int main(){

    int i=0;
    int arr[42] = {0, };
    int input = 0;
    int count = 0;

    for(i=0; i<10; i++){
        scanf("%d", &input);
        arr[input % 42]++;
    }

    for(i=0; i<42; i++){
        if(arr[i] != 0) count++;
    }

    printf("%d\n", count);

    return 0;
}