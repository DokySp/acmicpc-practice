#include <stdio.h>

int main(){

    int i=0, j=0, k;
    int arr[10] = {0, };
    int input = 0;
    int compare = 0;
    int count = 50;

    for(i=0; i<10; i++){
        scanf("%d", &input);
        arr[i] = input % 42;
    }

    for(i=0; i<10; i++){
        compare = arr[i];
        if(compare >= 50)
            continue;
        
        for(j=i+1; j<10; j++){
            if(compare == arr[j])
                arr[j] = count;
            
        }
        arr[i] = count;
        count++;

    }
    printf("%d\n", count-50);

    return 0;
}