var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0]
var res = ""
var code

var c1 = function(i) {
    return code[i] == 0 ? 2 : 3
}
var c2 = function(i) {
    return code[i] == 0 ? -1 : 1
}
var c3 = function(i) {
    return code[i] == 0 ? 4 : -1
}
var c4 = function(i) {
    return code[i] == 0 ? 5 : -1
}
var c5 = function(i) {
    return code[i] == 0 ? 5 : 6
}
var c6 = function(i) {
    if(code[i] == 1) return 6
    if(code[i] == 0 && code[i+1] == 1) return 1
    if(code[i] == 1 && code[i+1] == 0) return 4
}

var auto = [undefined, c1, c2, c3, c4, c5, c6]

for(var T=1; T<=tc; T++){

    code = inp[T]
    console.log(code[0]-0)
    var next = auto[1](i)

    for(var i=1; i<code.length; i++){
        console.log(next)
        next = auto[next](i)
        if(next == -1){
            break;
        } 
    }
    console.log(next)
    if(next == 1 || next == 6){
        res += "YES\n"
    } else {
        res += "NO\n"
    }
}

console.log(res)