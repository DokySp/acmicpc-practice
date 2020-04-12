#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%.9lf", (double)a/b);
    // 문제 조건 중,
    // > 실제 정답과 출력값의 절대오차 또는 상대오차가 10^-9 이하이면 정답이다.
    // 위 조건이 있기 때문에 자릿수를 일단 출력해주어야 하는 듯..
}