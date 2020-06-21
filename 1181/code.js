
var fs = require('fs')

var inp = fs.readFileSync('input').toString().split("\n")
var res = []
var resCount = 0;
var maxLen = 0;
inp.splice(0,1)

for(i=0; i<inp.length; i++)
    if(maxLen < inp[i].length) maxLen = inp[i].length


for(i=1; i<=maxLen; i++){
    var tmp = []
    for(j=0; j<inp.length; j++)
        if(inp[j].length == i)
            tmp.push(inp[j])

    tmp.sort()

    for(j=0; j<tmp.length; j++) res[resCount++] = tmp[j]
}


for(i=1; i<res.length; i++){
    if(res[i-1] == res[i]){
        res.splice(i-1,1)
        i--
        // 계속해서 중복을 확인 & 제거
    }
}

for(i=0; i<res.length; i++)
    console.log(res[i])