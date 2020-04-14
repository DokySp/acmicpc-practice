// 14:41 .83

#include <stdio.h>
#include <stdlib.h>
#define MAX_PATH 35

int pop();
void push(int);
void resetPath(int, int);
void resetStack();
int getLast();

int stack[30] = {0, };
int stackLength = 1;
int path[MAX_PATH][MAX_PATH] = {{0,},};

int main(){

    int tc = 0;
    int i=0, j=0, T=0;
    int n, m = 0;
    int compare = 0;
    int res = 0;

    scanf("%d", &tc);

    for(T=0; T<tc; T++) {

        scanf("%d", &n);
        scanf("%d", &m);

        // reset path array
        resetPath(n, m);
        // reset stack
        resetStack();
        res = 0;
        i = 0;


        while(stackLength > 0){
            compare = getLast();
            if(path[i][compare] == -1){  // 0. undefined
                pop();
                push(pop()+1);
                i--;
            }
            else if(path[i][compare+1] == -1 && i == n-1){  // 1. in last n, 오른쪽이 없는 경우,
                path[i][compare]++;
                pop();
                push(pop()+1);
                i--;
            }
            else if(path[i+1][compare+1] != -1){  // 2-1. 대각 아래가 있는 경우
                path[i][compare]++;
                i++;
                push(compare+1);
            }
            else {  // 2-2. 대각 아래가 없는 경우
                path[i][compare]++;
                push(pop()+1);
            }

        }


        for(i=0; i<m; i++){
            res += path[n-1][i];
        }

        printf("%d\n", res);

    }

    return 0;
}



int pop(){
    return stack[(stackLength--)-1];
}

void push(int inp){
    stack[stackLength] = inp;
    stackLength++;
}

int getLast(){
    return stack[stackLength-1];
}

void resetStack(){
    int i=0;
    for(i=1; i<30; i++){
        stack[i] = -1;
    }
    stack[0] = 0;
    stackLength = 1;
}

void resetPath(int n, int m){
    int i,j;
    for(i=0; i<MAX_PATH; i++){
        for(j=0; j<MAX_PATH; j++){
            path[i][j] = -1;
        }
    }
    for(i=0; i<n; i++){
        for(j=0; j<m; j++){
            if(m-n < j-i)
                continue;
            else
                path[i][j] = 0;
        }
    }
}