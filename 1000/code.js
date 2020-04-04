
var fs = require("fs");

var inp = fs.readFileSync("/dev/stdin").toString();
//var inp = fs.readFileSync("./input.txt").toString();

console.log(Number.parseInt(inp.split(' ')[0])+Number.parseInt(inp.split(' ')[1]))