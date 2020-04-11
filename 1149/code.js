
// var inp = require('fs').readFileSync('/dev/stdin').toString().split('\n')
var inp = require('fs').readFileSync('./input').toString().split('\n')

var colorNum = inp[0]

var prevColor = inp[1].split(' ').map((v)=>{return parseInt(v)})

for(var C=1; C<colorNum; C++){

    var currColor = inp[C+1].split(' ').map((v)=>{return parseInt(v)})
    
    for(var i=0; i<3; i++){
        var compare = []
        for(var j=0; j<3; j++)
            if(i!=j){
                compare[compare.length] = prevColor[j]
            }
        
        compare[0] < compare[1] ? currColor[i]+= compare[0] : currColor[i]+= compare[1]
    }
    prevColor = currColor
}

// 마지막 배열 정보에서 최솟값을 찾는다.
var min = prevColor[0]
for(var i=1; i < 3; i++)
    if(min > prevColor[i])
        min = prevColor[i]
console.log(min)
