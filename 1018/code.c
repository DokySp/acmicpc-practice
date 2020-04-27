#include <stdio.h>

int main(){

    int n, m, board[50][50] = {{0,},}, i, j, bin = 0, resb=0, resw=0, sti, stj, min = 1000000000;
    char inp[51];

    scanf("%d %d", &n, &m);

    for(i=0; i<n; i++){
        scanf("%s", inp);
        j = 0;
        while(inp[j] != '\0'){
            if(inp[j] == 'W'){
                board[i][j++] = 2;
            }
            else if(inp[j] == 'B'){
                board[i][j++] = 1;
            }
        }
    }

    for(sti = 0; sti <= n-8; sti++){
        for(stj = 0; stj <= m-8; stj++){

            resw = 0;
            resb = 0;

            // 검은색으로 먼저 시작 시
            bin = 1;
            for(i=sti; i<8+sti; i++){
                for(j=stj; j<8+stj; j++){
                    if(board[i][j] == bin) resb++;
                    bin = (bin == 1) ? 2 : 1;
                }
                bin = (bin == 1) ? 2 : 1;
            }

            // 흰색으로 먼저 시작 시
            bin = 2;
            for(i=sti; i<8+sti; i++){
                for(j=stj; j<8+stj; j++){
                    // printf("%d ", board[i][j]);
                    if(board[i][j] == bin) resw++;
                    bin = (bin == 1) ? 2 : 1;
                }
                // printf("\n");
                bin = (bin == 1) ? 2 : 1;
            }

            resw = resw < resb ? resw : resb;
            min = min > resw ? resw : min;

        }
    }
    
    printf("%d\n", min);

    return 0;
}