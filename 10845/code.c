#include <stdio.h>
#include <string.h>

void push(int *, int);
int pop(int *);
int size(int *);
int empty(int *);
int front(int *);
int back(int *);


int main(){

    int tc;
    int num;
    char inp[20];
    int queue[10001] = {0, };

    scanf("%d", &tc);

    while(tc--){
        scanf("%s", inp);
        if(inp[0] == 'p' && inp[1] == 'u') scanf("%d", &num);

        if(strcmp(inp, "push") == 0){
            push(queue, num);
        } else if(strcmp(inp, "pop") == 0){
            printf("%d\n", pop(queue));
        } else if(strcmp(inp, "size") == 0){
            printf("%d\n", size(queue));
        } else if(strcmp(inp, "empty") == 0){
            printf("%d\n", empty(queue));
        } else if(strcmp(inp, "front") == 0){
            printf("%d\n", front(queue));
        } else if(strcmp(inp, "back") == 0){
            printf("%d\n", back(queue));
        }

    }
    return 0;
}



void push(int *queue, int item){
    queue[size(queue)] = item;
}

int pop(int *queue){
    if(empty(queue)) return -1;

    int i = 0;
    int item = queue[0];
    int sizeQ = size(queue);
    // 당기기
    for(i=0; i<sizeQ; i++) queue[i] = queue[i+1];
    
    return item;
}

int size(int *queue){
    int i = 0;
    while(queue[i] != 0) i++;
    return i;
}

int empty(int *queue){
    if(queue[0] == 0) return 1;
    else return 0;
}

int front(int *queue){
    if(empty(queue)) return -1;
    return queue[0];
}

int back(int *queue){
    if(empty(queue)) return -1;
    return queue[size(queue)-1];
}