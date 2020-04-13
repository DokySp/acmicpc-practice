
var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0] - 0

for (var T = 1; T <= tc; T++) {

    var tmp = inp[T].split(' ')
    var path = []

    var n = tmp[0] - 0
    var m = tmp[1] - 0

    for (var i = 0; i < n; i++) {
        var pp = []
        for (var j = 0; j < m; j++) {
            if (m - n < j - i)
                pp.push(undefined)
            else
                pp.push(0)
        }
        path.push(pp)
    }


    var stack = [0]
    var i=0 // n (세로)
    var j=0 // m (가로)

    for (var V = 0; V < 24; V++) {
        // 스택에서 뺀 값이...
        // 1. 오른쪽이 없는 경우,
        //   -> 스택에서  2개 빼고, 마지막꺼 +1해서 추가 (path++)
        // 2-1. 대각 아래가 있는 경우
        //   -> 아래로 내려감, 스택 에 추가 (path++)
        // 2-2. 대각 아래가 없는 경우
        //   -> 스택에서  1개 빼고, +1해서 추가 (path++)

        var compare = stack[stack.length-1]

        // 1.
        if ( path[i][compare+1] == undefined){
            path[i][compare]++
            stack.pop()
            stack.push(stack.pop()+1)
            i--
            console.log("1")
        }
        else if( path[i+1] != undefined && path[i+1][compare+1] != undefined ){ // 2-1.
            console.log("2")
            path[i][compare]++
            i++
            stack.push(compare+1)
        } else { // 2-2.
            console.log("3")
            path[i][compare]++
            stack.push(stack.pop()+1)
        }

        console.log(stack)
        console.log()

    }

    console.log(path)


}



