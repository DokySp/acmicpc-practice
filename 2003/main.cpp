#include <iostream>

int main(){
    int n = 0, m=0;
    int item[10000] = {0,};

    std::cin >> n;
    std::cin >> m;


    for(int i=0; i<n; i++)
        std::cin >> item[i];

    int checker = 0;
    int addCounter = 0;

    for(int i=0; i<n; i++){
        
        for(int x=0; checker < m; x++){
            checker += item[i+x];
        }
        if(checker == m){
            addCounter++;
            checker = 0;
        } else {
            checker = 0;
        }

    }

    std::cout << addCounter << std::endl;

    return 0;
}