#include <stdio.h>
#include <string.h>

int main(){

    char words[1000001] = {0, };
    int i=0, len;
    int count = 1;

    // fgets(words, 1000001, stdin);
    gets(words);
    len = strlen(words);

    // trim
    for(i=0; i<1000001; i++){
        if(words[i] == 32) words[i] = 1;
        else break;
    }
    for(i=len-1; i>=0; i--){
        if(words[i] == 1) count = 0;
        if(words[i] == 32) words[i] = 1;
        else break;
    }

    // space => 32
    for(i=0; words[i] != '\0'; i++){
        if(words[i] == 32) count++;
    }

    printf("%d\n", count);

    return 0;
}