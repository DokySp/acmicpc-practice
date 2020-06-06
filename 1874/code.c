#include <stdio.h>
#define ST_MAX_LEN 11

void push(int *, int);
int pop(int *);
int isEmpty(int *);
int getLen(int *);

int main(){

    int i;
    int tc = 0;
    int n[ST_MAX_LEN] = {0, };
    int stack[ST_MAX_LEN] = {0, };

    // scanf("%d", &tc);

    // for(i=0; i<tc; i++) scanf("%d", &n[i]);




    // Stack Test Code
    // while(1){
    //     scanf("%d", &tc);
    //     switch(tc){
    //         case 1: scanf("%d", &tc); push(stack, tc); break;
    //         case 2: printf("%d\n", pop(stack)); break;
    //         case 3: printf("%d\n", isEmpty(stack)); break;
    //         case 4: printf("%d\n", getLen(stack)); break;
    //     }
    //     for(i=0; i<ST_MAX_LEN; i++){
    //         printf("%d ", stack[i]);
    //     }
    //     printf("\n");
    // }

    return 0;
}


void push(int *stack, int item){
    stack[getLen(stack)] = item;
}

int pop(int *stack){
    int item=0, len = getLen(stack)-1;
    if(isEmpty(stack)) return -1;

    item = stack[len];
    stack[len] = 0;
    return item;
}

int isEmpty(int *stack){
    if(stack[0] == 0) return 1;
    return 0;
}

int getLen(int *stack){
    int i = 0;
    while(i<ST_MAX_LEN){
        if(stack[i] == 0) return i;
        i++;
    }
    return ST_MAX_LEN;
}