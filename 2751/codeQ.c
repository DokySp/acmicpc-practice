#include <stdio.h>

int main(){

    int inp, size;
    int i=0;
    int list[1000000] = {0, };

    scanf("%d", &inp);
    size = inp;
    while(inp--)
        scanf("%d", &list[size-(inp+1)]);
    
    


    return 0;
}