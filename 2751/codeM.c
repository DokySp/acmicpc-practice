#include <stdio.h>


void merge(int*, int, int, int);

int main(){

    int inp, size;
    int i=0, n=0;
    int list[1000000] = {0, };

    int intv = 1;


    scanf("%d", &inp);
    size = inp;
    while(inp--)
        scanf("%d", &list[size-(inp+1)]);
    
    

    while(1){
        if(intv >= size) break;

        for(i=0; i<size;){
            if(i+intv >= size) break;

            merge(list, i, i+intv, size);
            i = i+intv*2;
        }

        intv *= 2;
    }

    for(i=0; i< size; i++) printf("%d\n", list[i]);
    
    return 0;
}


void merge(int* arr, int L, int R, int size){

    int i = 0, n = 0;
    int tmp[1000000] = {0, };
    int comp = (R-L)*2;
    int maxL = R-1;
    int maxR = ( R+(R-L)-1 > size ) ? size-1 : R+(R-L)-1;
    int st = L;

    for(i=0; i < comp; i++){

        if(L > maxL){
            tmp[i] = arr[R];
            R++;
            continue;
        } else if(R > maxR) {
            tmp[i] = arr[L];
            L++;
            continue;
        }

        if(arr[L] > arr[R]) {
            tmp[i] = arr[R];
            R++;
        } else if(arr[L] < arr[R]) {
            tmp[i] = arr[L];
            L++;
        } else {
            tmp[i++] = arr[R];
            tmp[i] = arr[L];
            R++;
            L++;
        }
    }

    for(i=st; i<=maxR; i++)
        arr[i] = tmp[n++];
    

}