// Not work on BOJ(Runtime Error)
var process = require("process");

var res = ""

process.stdin.on("data", function(inp) {

    // Buffer changed when user input enter key
    
    var len = inp.length
    var a = 0;
    var b = 0;

    for(var i=0; i<len; i++){

        switch(inp[i]){

            case 10: // "CRLF"
                if(b == 0)
                    break;
                res += a+b+"\n"
                break
            case 32: // " "
                b = a
                a = 0
                break
            default: // number
                a = a*10 + (inp[i]-48)

        }
    }
})
process.stdin.end(() => {
    console.log("res: ", res)
})