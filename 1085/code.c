#include <stdio.h>

int main(){

    int i, j, x, y, w, h;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    // 오른쪽에 있을 떄
    if(w/2.0 <= x){  // 그냥 /2를 해주면 둘 다 int이기 때문에 나머지가 1.5가 아닌 1이 나온다!
        x = w - x;
    }

    // 위쪽에 있을 때
    if(h/2.0 <= y){
        y = h - y;
    }

    printf("%d\n", x > y ? y : x );
    

    return 0;
}