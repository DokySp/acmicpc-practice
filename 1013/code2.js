

var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0]
var res = ""

for(var T=1; T<=tc; T++){

    var code = inp[T]
    var sep = []
    var tmp = ""
    var ans = 0

    for(var i=0; i<code.length; i++){
        if(i != code.length-1 && code[i] == 0 && code[i+1] == 1){ // 01
            tmp != "" ? sep.push(tmp) : true
            tmp = ""
            sep.push("01")
            i++
        } else if(i != code.length-1 && code[i] == 1 && code[i+1] == 0){ // 10
            tmp != "" ? sep.push(tmp) : true
            tmp = ""
            sep.push("10")
            i++
        } else {
            tmp += code[i]
        }
    }
    tmp != "" ? sep.push(tmp) : true

    console.log("A", sep)

    var isZero = true


    // 애초에 10과 01을 먼저 구별할 경우,
    // 100110 <- NO가 뜨게 된다..
    // 정답: 10011 01
    // 오답: 1001 101 (10 01 10 1 이렇게 분리됨.)
    while(isZero == true){
        isZero = false
        for(var i=0; i<sep.length; i++){
            if(i != sep.length-1 && sep[i][sep[i].length-1] == 0){
                isZero = true
                sep[i] = sep[i] + sep[i+1]
                sep.splice(i+1, 1)
            }
        }
    }

    console.log("B", sep)

    for(var i=0; i< sep.length; i++){
        if(sep[i] == "01") sep[i] = 'B'
        else if(sep[i].substring(0,3) == "100" && sep[i][sep[i].length-1] == "1") sep[i] = 'A'
        // ~~위의 분류방식으로 마지막이 무조건 1로 끝난다!~~
        // 반례 => 1000 / 10 00 / A 00 -> 정답X
        // 마지막에 1로 끝나는지를 검사하는 조건 추가!
        else if(sep[i][0] == 1 && sep[i][1] == 1) sep[i] = "1"
        else {
            ans = -1
            break
        }
    }

    console.log("C", sep, ans)
    console.log()

    if(ans != -1){
        for(var i=0; i<sep.length-1; i++){
            if(sep[i] == "B" && sep[i+1] == "1"){
                ans = -1
                break;
            }
        }
    }
    res += (ans == 0 ? "YES" : "NO") +"\n"
}

console.log(res)