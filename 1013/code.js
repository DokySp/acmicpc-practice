// var inp = require('fs').readFileSync('/dev/stdin').toString().split('\n')
var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0]
var res = ""


var s1 = function(next1, next2) {
    if(next1 == 0 && next2 == 1) return 12 //01 (to 1)
    else if(next1 == 1) return 2
    else return -1
}
var s2 = function(next1, next2) {
    if(next1 == 0 && next2 == 0) return 3
    else return -1
}
var s3 = function(next1) {
    if(next1 == 1) return 4
    else if(next1 == 0) return 3
    else return -1
}
var s4 = function(next1, next2, next3) {
    if(next1 == 1 && next2 == 0 && next3 == 0) return 33 // 100 (to 3)
    else if(next1 == 1 && next2 == 0 && next3 == 1) return 13  // 101 (to 1)
    else if(next1 == 0 && next2 == 1) return 12 // 01 (to 1)
    else if(next1 == 1) return 4 // 1
    else return -1
}

var auto = [undefined, s1, s2, s3, s4]

for(var T=1; T<=tc; T++){

    var code = inp[T]
    code += "FF" // dummy for protect overflow
    // console.log(code)

    var next = auto[1](code[0], code[1])

    if(next > 10) next = Number.parseInt(next/10)

    for(var i = (next==1?2:1); i<code.length-2 && next != -1; i++){ // -2: disable dummy
        // console.log("1:", next)
        next = auto[next](code[i], code[i+1], code[i+2])

        if(next > 10){
            i += next%10-1 // -1: for i++ prevent
            next = Number.parseInt(next/10)
        }
         
    }
    // console.log(next)
    if(next == 1 || next == 4){
        res += "YES\n"
        // console.log("YES")
    } else {
        res += "NO\n"
        // console.log("NO")
    }
}

console.log(res)