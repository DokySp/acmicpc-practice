#include <stdio.h>

int main(){

    char inp[6], len, start, end;

    while(1){

        scanf("%s", inp);

        if(inp[0] == '0') break;

        for(len = 0; len < 6; len++){
            if(inp[len] == 0) break;
        }

        start = 0;
        end = len-1;

        for(len=0; ;len++){
            if(inp[start] != inp[end]){
                printf("no\n");
                break;
            }
            if(start>=end){
                printf("yes\n");
                break;
            }
            start++;
            end--;
        }

    }

    return 0;
}