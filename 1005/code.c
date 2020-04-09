#include <stdio.h>
#include <stdlib.h>
#include <malloc.h> 

int main(){


    int testCase = 0;
    int T, i, c = 0;
    
    int nodeNum = 0;
    int edgeNum = 0;
    int tmp = 0;

    typedef struct nod {
        int time;
        int from;
        int* to;
        int toLen;
        int* timeTmp;
        int timeTmpLen;
    } Node;

    Node *node;

    int *ee;// = (int *)malloc(sizeof(int)*2);
    ee[0] = 1;
    ee[1] = 1;
    ee[4000] = 1;
    printf("%d", ee[4000]);

    scanf("%d", &testCase);
    
    for(T=0; T<testCase; T++){

        // N, K 입력 받기
        scanf("%d %d", &nodeNum, &edgeNum);

        node = (Node *)calloc(nodeNum, sizeof(Node));

        // 건설 시간 입력
        for(i=0; i<nodeNum; i++){
            scanf("%d", &node[i].time );
            node[i].from = 0;
            node[i].to = (int*)malloc(0);
            node[i].toLen = 0;
            node[i].timeTmp = (int*)malloc(0);
            node[i].timeTmpLen = 0;
        }

        

        for(i=0; i<edgeNum; i++){
            // scanf("%d", &tmp );
            // scanf("%d", &tmp );
            // printf("%d", (int)malloc_usable_size(node[tmp].to)-1);
            // node[tmp].to[malloc_usable_size(node[tmp].to)-1] = tmp;
        }

        





    }






}