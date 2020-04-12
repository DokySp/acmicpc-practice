#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){

    char res[1000] = "cp -r 'scaffold (build 0000)' ";
    int i = 0;
    int l = 30;

    while(argv[1][i] != '\0')
        res[l++] = argv[1][i++];
    
    printf("\n*%s번 문제를 위한 폴더를 생성합니다.\n", argv[1]);
    system(res);

    i=0;
    l=0;
    while(argv[1][i] != '\0'){
        if(l == 0) res[l++] = 'l';
        else if(l == 1) res[l++] = 's';
        else if(l == 2) res[l++] = ' ';
        else res[l++] = argv[1][i++];
    }
    res[l] = '\0';

    system(res);
    printf("\n*새로 생성된 프로젝트 폴더를 확인 후 이동하세요.\n");
    res[0] = 'c'; res[1] = 'd';
    printf("  ➡️  $ %s", res);
    printf("\n\n*오늘도 즐코하세요!.\n\n\n");
    return 0;
}