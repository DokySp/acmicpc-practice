#include <stdio.h>

int main(){
    int len = 0;
    int sum = 0;
    int i;
    char inp[101] = {0, };

    scanf("%d", &len);
    scanf("%s", inp);
    for(i=0; i<len; i++)
        sum += inp[i]-'0';

    printf("%d\n", sum);

    return 0;
}