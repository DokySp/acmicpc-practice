// 31:11 .63 
// 46:25 .02
// 33.27 .67

var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0] - 0
var resStr = ""

for (var T = 1; T <= tc; T++) {

    var tmp = inp[T].split(' ')
    var path = []

    var n = tmp[0] - 0
    var m = tmp[1] - 0

    for (var i = 0; i < n; i++) {
        var pp = []
        for (var j = 0; j < m; j++) {
            if (m - n < j - i)
                pp[j] = undefined
            else
                pp[j] = 0
        }
        path[i] = pp
    }


    var stack = [0]
    var i=0 // n (세로)
    var j=0 // m (가로)

    while (i >= 0) {
        // 스택에서 뺀 값이...
        // 0. undefined
        //   -> same as 1.
        // 1. in last n, 오른쪽이 없는 경우,
        //   -> 스택에서  2개 빼고, 마지막꺼 +1해서 추가 (path++)
        // 2-1. 대각 아래가 있는 경우
        //   -> 아래로 내려감, 스택 에 추가 (path++)
        // 2-2. 대각 아래가 없는 경우
        //   -> 스택에서  1개 빼고, +1해서 추가 (path++)

        var compare = stack[stack.length-1]

        if( path[i][compare] == undefined ){
            // path[i][compare]++

            // stack.pop()
            // stack.push(stack.pop()+1)
            // 위에 코드를 아래로 바꿈
            stack.length -= 1
            stack[stack.length-1]++

            i--
            // console.log("0. undefined")
        }
        else if ( path[i][compare+1] == undefined && i == n-1 ){  // 1.
            path[i][compare]++

            // stack.pop()
            // stack.push(stack.pop()+1)
            // 위에 코드를 아래로 바꿈
            stack.length -= 1
            stack[stack.length-1]++

            i--
            // console.log("1. right X")
        }
        else if( path[i+1] != undefined && path[i+1][compare+1] != undefined ){ // 2-1.
            // console.log("2. right down O")
            // path[i][compare]++    // 속도에 별 영향은 없지만... 안써도 정답은 나온다.
            i++

            // stack.push(compare+1)
            // 위에 코드를 아래로 바꿈
            stack[stack.length] = compare+1

        } else { // 2-2.
            // console.log("3. right down X")
            path[i][compare]++

            // stack.push(stack.pop()+1)
            // 위에 코드를 아래로 바꿈
            stack[stack.length-1]++
        }


        // console.log(path)
        // console.log(stack)
        // console.log()

    }

    var res = 0
    for(var i=0; i<m; i++)
        res += path[n-1][i]
    
    resStr += res + "\n"
    
}

console.log(resStr)
