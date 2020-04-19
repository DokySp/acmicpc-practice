#include <stdio.h>

int main(){

    int song[8] = {0, };
    int i, res, ase = 0, compare = 1;

    for(i=0; i<8; i++)
        scanf("%d", &song[i]);

    for(i=0; i<8; i++){
        if(i == 0){
            if(song[0] == 1){
                compare = 1;
                ase = 1;
                res = 1;
            } else if(song[0] == 8) {
                compare = 8;
                ase = -1;
                res = 2;
            } else {
                res = 3;
                break;
            }
        }

        if(song[i] == compare){
            compare += ase;
            
        } else {
            res = 3;
            break;
        }

    }

    switch(res){
        case 1: printf("ascending\n"); break;
        case 2: printf("descending\n"); break;
        case 3: printf("mixed\n"); break;
    }
    return 0;
}