var fs = require("fs")

var inp = fs.readFileSync("/dev/stdin").toString().split(/[\s,]+/)
// var inp = fs.readFileSync("./input").toString().split(/[\s,]+/)

var ts = inp[0]-0
var res = "";

for(var T=1; T<=ts*2; T+=2)
	res += (inp[T]-0) + (inp[T+1]-0) + '\n'

console.log(res)

