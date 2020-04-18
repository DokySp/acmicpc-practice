
var inp = require('fs').readFileSync('/dev/stdin').toString().split('\n')
// var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0]
var resStr = ""

for(var T=0; T<tc; T++){
    var x = inp[T+1].split(' ')
    var y = x[1]-0
    x = x[0]-0

    var distance = y-x
    var count = 0
    var jumpMaxHalf = 0

    for(var i=1; ; i++){

        count += i

        if(count >= distance/2 ){
            count = i
            break
        }
    }

    for(var i=1; i<=count; i++)
        jumpMaxHalf+=i

    if(jumpMaxHalf*2-distance >= count )
        count = count*2-1
    else
        count = count*2

    resStr += count + "\n"
}

console.log(resStr)