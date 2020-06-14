#include <stdio.h>

int main(){

    int n=0, m=0;
    int i=0, s=0, u=0;
    int a=0, b=0, c=0, d=0;

    int coor[1001][1001] = {{0, }, }; // 죄표는 1000 이하의 자연수!
    int btn[50] = {0, };


    scanf("%d %d", &n, &m);

    for(i=0; i<n; i++){ // 버튼 위치 받기 (50 이하)
        scanf("%d %d %d %d", &a, &b, &c, &d);
        for(s=a; s<=b; s++){
            for(u=c; u<=d; u++){
                coor[s][u] = i+1;
            }
        }

    }


    for(i=0; i<m; i++){ // 클릭 위치 받기 (1000 이하)
        scanf("%d %d", &a, &b);
        btn[coor[a][b]]++;
    }

    for(i=1; i<=n; i++){ // 클릭 위치 받기 (1000 이하)
        printf("Button #%d: %d\n", i+1, btn[i]);
    }


    return 0;
}