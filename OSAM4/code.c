#include <stdio.h>

int main(){

    char word[100001] = {0, };
    int len = 0, q = 0;
    int checker[26] = {0, };
    int max = -1, maxIndex = 0;

    int st, en;
    int i=0, k=0;

    scanf("%d %d", &len, &q);
    gets(word); //scanf에서 개행 입력을 못 받고 넘기는 것을 받아줌.
    gets(word);

    for(i=0; i<q; i++){
        scanf("%d %d", &st, &en);

        for(k=st-1; k<en; k++){
            checker[word[k]-'A']++;
        }

        for(k=25; k>=0; k--){
            if(checker[k] >= max) { 
                max = checker[k];
                maxIndex = k;
            }
        }
        
        printf("%c\n", maxIndex+'A');
        // 초기화
        for(k=0; k<26; k++) checker[k] = 0;
        max = -1;
        maxIndex = 0;
    }
    
    return 0;
}
