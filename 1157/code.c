#include <stdio.h>
#include <string.h>

// 런타임 에러 
//   -> int main() 함수에 return 0; 이 아니면 
//      런타임 에러가 발생한다!

int main(){

    char input[1000001] = {0, };
    int alpha[26] = {0, };
    int maxAlpha = -1, max = -1, i;

    scanf("%s", input);

    for(i=0; input[i] != 0; i++){
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

    return 0;
}