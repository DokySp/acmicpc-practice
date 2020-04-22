#include <stdio.h>

int main(){

    int h, m;

    scanf("%d %d", &h, &m);
    m += h*60;

    m -= 45;

    if(m < 0)
        m += 1440;

    printf("%d %d\n", m/60, m%60);


    return 0;
}