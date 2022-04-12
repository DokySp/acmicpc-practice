#include <iostream>

int alphaCount[26] = {3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1};
char aName[101] = "";
char bName[101] = "";
char name[202] = "";


int main(){
    
    int aLen, bLen, tmpLen;

    std::cin >> aLen;
    std::cin >> bLen;

    for(int i=0; i < aLen; i++) std::cin >> aName[i];
    for(int i=0; i < bLen; i++) std::cin >> bName[i];
    
    for(int i=0; i < aLen; i++) aName[i] = alphaCount[(int)(aName[i] - 65)];
    for(int i=0; i < bLen; i++) bName[i] = alphaCount[(int)(bName[i] - 65)];


    // for(int i=0; i < aLen; i++) std::cout << (int)aName[i] << " ";
    // std::cout << std::endl;
    // for(int i=0; i < bLen; i++) std::cout << (int)bName[i] << " ";
    // std::cout << std::endl;std::cout << std::endl;

    if(aLen-bLen < 0) tmpLen = aLen;
    else tmpLen = bLen;

    for(int i=0; i < tmpLen; i++)
        name[i*2] = aName[i];
    
    for(int i=0; i < tmpLen; i++)
        name[(i*2)+1] = bName[i];
    
    if(aLen-bLen < 0){ // b가 더 길 때
        int i;
        for(i = 0; i<bLen-aLen; i++) name[(aLen*2)+i] = bName[aLen+i];
        name[(aLen*2)+i] = -1;
        tmpLen = (aLen*2)+i;
    }
    else{ // a가 더 길 때
        int i;
        for(i = 0; i<aLen-bLen; i++) name[(bLen*2)+i] = aName[bLen+i];
        name[(bLen*2)+i] = -1;
        tmpLen = (bLen*2)+i;
    }
    
    // for(int n=0; n<tmpLen+1; n++) std::cout << (int)name[n] << " ";
    // std::cout << std::endl;std::cout << std::endl;

    while(name[2] != -1){
        int i;
        for(i=0; name[i] != -1; i++) name[i] = (name[i] + name[i+1])%10;
        name[i-1] = -1;
        // for(int n=0; n<tmpLen; n++) std::cout << (int)name[n] << " ";
        // std::cout << std::endl;
    }

    std::cout << (int)name[0]*10 + (int)name[1] << "%" << std::endl;

    return 0;

}