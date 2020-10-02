#include <iostream>

using namespace std;

int main(){
    
    int bin[30] = {0,};
    int length = 0;
    int input;

    cin >> input;

    for(int i=0; i<30 && input != 1; i++){
        bin[i] = input % 2;
        input /= 2;
        length++;
    }

    bin[length] = 1; 
    
    int adder = 1;
    int result = 0;

    for(int i = length; i>= 0; i--){
        result += bin[i]*adder;
        adder *= 2;
    }

    cout << result << endl;

}