#include <stdio.h>

int main(){

    int test_case = 0;
    int T = 0;
    int score[1000] = {0,};
    int max = -1;
    double avg = 0.0;

    scanf("%d", &test_case);

    for(T=0; T<test_case; T++){
        scanf("%d", &score[T]);
        if(score[T] > max){
            max = score[T];
        }
    }

    for(T=0; T<test_case; T++){
        avg += score[T]/(double)max * 100;
    }
        
    
    printf("%.3lf\n", avg/T);

    return 0;

}