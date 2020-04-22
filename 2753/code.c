#include <stdio.h>

int main(){
    int i;
    scanf("%d", &i);
    printf("%d\n", (i%4==0 && i%100) || i%400==0 !=0 ? 1 : 0);
    return 0;
}