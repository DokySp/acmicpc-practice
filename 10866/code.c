#include <stdio.h>
#include <string.h>

void push_front(int *, int);
void push_back(int *, int);
int pop_front(int *);
int pop_back(int *);
int size(int *);
int empty(int *);
int front(int *);
int back(int *);


int main(){

    int deque[10001] = {0, };
    int tc, num;
    char inp[21];

    scanf("%d", &tc);
    while(tc--){
        scanf("%s", inp);
        if(inp[0] == 'p' && inp[1] == 'u') scanf("%d", &num);

        if(strcmp(inp, "push_back") == 0){
            push_back(deque, num);
        } else if(strcmp(inp, "push_front") == 0){
            push_front(deque, num);
        } else if(strcmp(inp, "pop_back") == 0){
            printf("%d\n", pop_back(deque));
        } else if(strcmp(inp, "pop_front") == 0){
            printf("%d\n", pop_front(deque));
        } else if(strcmp(inp, "size") == 0){
            printf("%d\n", size(deque));
        } else if(strcmp(inp, "empty") == 0){
            printf("%d\n", empty(deque));
        } else if(strcmp(inp, "front") == 0){
            printf("%d\n", front(deque));
        } else if(strcmp(inp, "back") == 0){
            printf("%d\n", back(deque));
        }

    }


    return 0;
}

void push_front(int *deque, int item){
    int sizeD = size(deque);
    while(sizeD--) deque[sizeD+1] = deque[sizeD];
    deque[0] = item;
}

void push_back(int *deque, int item){
    deque[size(deque)] = item;
}

int pop_front(int *deque){
    if(empty(deque)) return -1;

    int i;
    int sizeD = size(deque);
    int item = deque[0];
    for(i=0; i<sizeD; i++) deque[i] = deque[i+1];
    return item;
}

int pop_back(int *deque){
    if(empty(deque)) return -1;
    int item = deque[size(deque)-1];
    deque[size(deque)-1] = 0;
    return item;
}

int size(int *deque){
    int i = 0;
    while(deque[i] != 0) i++;
    return i;
}

int empty(int *deque){
    if(deque[0] == 0) return 1;
    else return 0;
}

int front(int *deque){
    if(empty(deque)) return -1;
    return deque[0];
}

int back(int *deque){
    if(empty(deque)) return -1;
    return deque[size(deque)-1];
}