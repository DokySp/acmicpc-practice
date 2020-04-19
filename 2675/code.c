#include <stdio.h>

int main(){

    int T, c, i, tc, rep = 0;
    char str[21] = {0, };

    scanf("%d", &tc);

    for(T=0; T<tc; T++){
        
        scanf("%d %s", &rep, str);

        for(c=0; str[c] != '\0'; c++){

            for(i=0; i<rep; i++)
                printf("%c", str[c]);

        }
        printf("\n");
    }

    return 0;
}