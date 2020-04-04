
var fs = require("fs")

var inp = fs.readFileSync("/dev/stdin").toString().split(' ');

console.log(Number.parseInt(inp[0])-Number.parseInt(inp[1]))