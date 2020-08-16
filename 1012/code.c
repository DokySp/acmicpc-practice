#include <stdio.h>



int find(int grid[][51], int x, int y, int mx, int my){
    
    // 오른쪽
    if(x+1 < mx && grid[x+1][y] == 1) {
        grid[x+1][y] = -1;
        find(grid, x+1, y, mx, my);
    }

    // 아래
    if(y+1 < my && grid[x][y+1] == 1) {
        grid[x][y+1] = -1;
        find(grid, x, y+1, mx, my);
    }

    // 왼쪽도 검사!!
    if(x-1 >= 0 && grid[x-1][y] == 1) {
        grid[x-1][y] = -1;
        find(grid, x-1, y, mx, my);
    }

    // 위쪽도 검사!! -> ⨆ 모양인 경우가 있음!
    if(y-1 >= 0 && grid[x][y-1] == 1) {
        grid[x][y-1] = -1;
        find(grid, x, y-1, mx, my);
    }

    grid[x][y] = -1;

    return -1;
}

// 초기화 안해주면 이전 값과 충돌!
void init(int grid[][51]){
    int i, j;
    for(i=0; i<51; i++)
        for(j=0; j<51; j++)
            grid[i][j] = 0;
    return;
}


int main(){
    int tc; 
    int x, y, sample;
    int i, j;
    int bx, by;
    int grid[51][51] = {{0, }};
    int count = 0;
    scanf("%d", &tc);

    while(tc--){
        count = 0;
        init(grid);

        scanf("%d %d %d", &x, &y, &sample);
        
        for(i=0; i<sample; i++){
            scanf("%d %d", &bx, &by);
            grid[bx][by] = 1;
        }

        // 바이너리 탐색
        // 좌상단에서 글 읽는 순서대로 검색하도록 수정
        for(j=0; j<y; j++){
            for(i=0; i<x; i++){
                // 배추가 있는 곳을 찾으면
                if(grid[i][j] == 1){
                    // printf("%d %d / ", i, j);
                    if(find(grid, i, j, x, y) == -1) count++;

                }
            }
        }

        printf("%d\n", count);
        
    }

    return 0;
}

