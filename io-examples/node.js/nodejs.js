
var fs = require("fs")

//동기적으로 파일 읽어오기
let input = fs.readFileSync("./input.txt").toString()
// **실제 구동 시, /dev/stdin 으로 바꾸어주어야 한다.**


console.log(input)
return;