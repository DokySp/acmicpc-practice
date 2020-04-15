var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0] - 0
var resStr = ""
const MAX_PATH = 29
var path = []

// 미리 테이블 만들어두기
for (var i = 0; i < MAX_PATH; i++) {
    var pp = []
    for (var j = 0; j < MAX_PATH; j++) {
        if (i == 0)
            pp[j] = 1
        else if (i == 1)
            pp[j] = j
        else if (i >= 2 && j >= 1) {
            pp[j] = path[i - 1][j - 1] + pp[j - 1]
        }
        else
            pp[j] = 0;
    }
    path[i] = pp
}

for (var T = 1; T <= tc; T++) {
    var tmp = inp[T].split(' ')

    var n = tmp[0] - 0
    var m = tmp[1] - 0
    var res = 0;

    for(var i=0; i < m; i++)
        res += path[n-1][i]
    
    resStr += res + "\n"
}

console.log(resStr)