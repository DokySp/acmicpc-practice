#include <stdio.h>

int main(){
    int i;
    scanf("%d", &i);
    
    if( 90 <= i && i <= 100) printf("A\n");
    else if( 80 <= i && i <= 89) printf("B\n");
    else if( 70 <= i && i <= 79) printf("C\n");
    else if( 60 <= i && i <= 69) printf("D\n");
    else printf("F\n");

    return 0;
}