
var inp = require('fs').readFileSync('input').toString().split('\n')
var tc = inp[0] - 0
var res = ""

for (var T = 1; T <= tc; T++) {
    var tmp = inp[T].split(' ')
    var n = tmp[0] - 0
    var m = tmp[1] - 0

    if(n == m){ // 연산량을 줄임!
        res += 1 + "\n"
    } else {
        res += comb(m,n) + "\n"
    }

}
console.log(res)


function comb(n, r){
    var res = 1
    var tmp = 1

    // 이걸 안해주면, 29C27 같이 큰 수가 될 때 오차가 생긴다!
    if(n/2 < r)
        r = n - r

    for(var i=n; i>= n-(r-1); i--)
        res *= i
    for(var i=r; i > 0; i--)
        tmp *= i
    return res/tmp
}