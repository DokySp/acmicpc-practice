#include <stdio.h>

int strlen(char*);

int main(){

    int tc = 0, i, T, score = 0, res=0;
    char quiz[81] = {0, };
    int len = 0;

    scanf("%d", &tc);

    for(T=0; T<tc; T++){
        scanf("%s", quiz);
        len = strlen(quiz);

        for(i=0; i<len; i++){
            if(quiz[i] == 'O'){
                score++;
                res += score;
            }
            else if(quiz[i] == 'X'){
                score = 0;
            }
        }

        printf("%d\n", res);
        res = 0;
        score = 0;

    }

    return 0;
}

int strlen(char *str){
    int i=0;
    while(str[i] != 0)
        i++;
    return i;
}