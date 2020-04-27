#include <stdio.h>
#define MAX_LEN 20000

int strcmpl(char *, char *, int);

int main(){

    char word[MAX_LEN][51];
    int len[MAX_LEN] = {0,};
    int sort[MAX_LEN] = {0,};
    int res[MAX_LEN] = {0,};
    int tc, i, leni, maxLen = -1, wl, countSort = 0, j, cmpRes, resLen = 0, resIndex = 0;;

    for(i=0; i<MAX_LEN; i++)
        res[i] = -1;

    scanf("%d", &tc);

    for(i=0; i<tc; i++){
        scanf("%s", word[i]);
        for(leni = 0; leni < 51; leni++){
            if(word[i][leni] == '\0'){
                len[i] = leni;
                if(maxLen < leni) maxLen = leni;
                break;
            }
        }
    }
        
    for(wl=1; wl<=maxLen; wl++){
        countSort = 0;

        for(i=0; i<MAX_LEN; i++)
            sort[i] = -1;

        // wl 길이만큼의 문자들 모음
        for(i=0; i<tc; i++){
            if(len[i] == wl){
                sort[countSort++] = i;
            }
        }

        if(countSort == 0) continue;

        // 버블소팅
        for(j=countSort-1; j > 0; j--){
            for(i=0; i<countSort-1; i++){
                // 결과값을 저장
                cmpRes = strcmpl(word[sort[i]], word[sort[i+1]], wl);
                if(cmpRes == 1){ // 뒤가 빠른 경우
                    cmpRes = sort[i+1];
                    sort[i+1] = sort[i];
                    sort[i] = cmpRes;
                } else if(cmpRes == 0){ // 둘이 같은 경우
                    sort[i+1] = -1; // 삭제
                }
            }
        }

        // 결과값을 담기
        for(i = 0; i < countSort; i++)
            if(sort[i] != -1) res[resIndex++] = sort[i];
            
    }


    // printf("\n");
    for(i=0; i<tc; i++){
        if(res[i] != -1) printf("%s\n", word[res[i]]);
    }
    
    return 0;
}


int strcmpl(char *a, char *b, int len){

    int i;

    for(i=0; i<len; i++){
        if(a[i] < b[i]) // a가 더 빠를 경우,
            return -1;
        else if(a[i] > b[i])  // b가 더 빠를 경우,
            return 1;
        else continue;
    }
     // 동일할 경우,
    return 0;
}
