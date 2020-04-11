
// var inp = require('fs').readFileSync('/dev/stdin').toString().split('\n')
var inp = require('fs').readFileSync('./input').toString().split('\n')

var colorNum = inp[0]
var res = 0
var prevSelect = -1

for(var C=0; C<colorNum; C++){

    var currColor = []
    var nextColor = -1
    var compare = []

    currColor = inp[C+1].split(' ')
    if(inp[C+2] != undefined){
        nextColor = inp[C+2].split(' ')
    }
    
    for(var i=0; i<3; i++){
        for(var j=0; j<3; j++){
            if(i == j){
                continue
            }
            if(i == prevSelect){
                compare[compare.length] = undefined
                continue
            }

            if(nextColor == -1){
                compare[compare.length] = parseInt(currColor[i])
            } else {
                compare[compare.length] = parseInt(currColor[i])+parseInt(nextColor[j])
            }
            
        }
    }

    // curr, next를 합쳤을 때 가장 큰 수를 계산한다.
    // 이 때, 같은 수가 나와도 크게 상관은 없는 듯하다.
    // -> 잘못 접근!
    // 3
    // 10 1 10
    // 1 10 100
    // 1 100 100
    // 정답은 21이지만, 다음 값만 비교해서 내려갈 경우,
    // 102가 결과로 나온다!
    // 
    // 즉, 이전값에 대한 정보를 계속 가지고 있는 상태에서
    // 계산을 타고 내려가야만 정답을 구할 수 있다! (DP!)

    var min = 2000000
    for(var i=0; i<6; i++){
        if(min > compare[i]){
            min = compare[i]
            prevSelect = i
        }
    }
    prevSelect = parseInt((prevSelect+0.5)/2)

    res += parseInt( currColor[ prevSelect ] )
}

console.log(res)