#include <stdio.h>
#include <string.h>

int push(int*, int);
int pop(int*);
int size(int*);
int empty(int*);
int top(int*);



int main(){

    int tc;
    char inp[30];
    int i = 0;
    int dec = 10;
    int num = 0;

    int stack[10000] = {0, };

    scanf("%d", &tc);

    while(tc--){
        scanf("%s", inp);
        if(inp[0] == 'p' && inp[1] == 'u') scanf("%d", &num);

        if(strcmp(inp, "push") == 0){
            push(stack, num);
        } else if(strcmp(inp, "pop") == 0){
            printf("%d\n", pop(stack));
        } else if(strcmp(inp, "size") == 0){
            printf("%d\n", size(stack));
        } else if(strcmp(inp, "empty") == 0){
            printf("%d\n", empty(stack));
        } else if(strcmp(inp, "top") == 0){
            printf("%d\n", top(stack));
        }

    }


    return 0;
}

int push(int* stack, int item){
    int lev = size(stack);
    stack[lev] = item;
    return 0;
}

int pop(int* stack){
    if(empty(stack)) return -1;

    int lev = size(stack)-1;
    int res = stack[lev];
    stack[lev] = 0;
    return res;
}

int size(int* stack){
    int i=0;
    while(stack[i] != 0) i++;
    return i;
}

int empty(int* stack){
    if(stack[0] == 0) return 1;  // emp
    else return 0;  // notEmp
}

int top(int* stack){
    if(empty(stack)) return -1;

    int lev = size(stack)-1;
    return stack[lev];
}