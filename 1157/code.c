#include <stdio.h>
#include <string.h>

// 01:00:48 .88 
// 씨발 런타임 에러 

void main(){

    char input[2000001] = {0, };
    int alpha[26] = {0, };
    int maxAlpha = -1, max = -1, i;
    int len = strlen(input);


    scanf("%s", input);
    
    for(i=0; i < len; i++){
        
        if(input[i] >= 'a'){
            alpha[input[i]-'a']++;
        } else {
            alpha[input[i]-'A']++;
        }  

    }

    for(i=0; i<26; i++){
        if(alpha[i] > max){
            max = alpha[i];
            maxAlpha = i;
        }
    }
    

    for(i=0; i<26; i++){
        if(alpha[i] == max && maxAlpha != i){
            maxAlpha = -1;
        }
    }

    if(maxAlpha == -1)
        printf("?\n");
    else
        printf("%c\n", maxAlpha+'A');

    return;
}