
var inp = require("fs").readFileSync("input").toString().split('\n')

var tc = inp[0]-0
var ans = ""

for(var T=1; T<=tc; T++){
    var tmp = inp[T].split(' ')
    var num = tmp[0]-0
    var rt = tmp[1]-1
    var res = num % 10;
    for(var i=0; i<rt; i++){
        res *= num;
        res %= 10;
    }
    if(res == 0) res = 10
    ans += res + "\n"
}

console.log(ans)