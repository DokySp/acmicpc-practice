
var fs = require("fs")

var inp = fs.readFileSync("/dev/stdin").toString().split("\n")
// var inp = fs.readFileSync("./input").toString().split("\n")

var ts = inp.splice(0,1)[0]

for(var T=0; T<ts; T++){
	
	var a = inp.splice(0,1)[0]
	var b = a.split(" ")[1]-0
	a = a.split(" ")[0]-0
	
	console.log(a+b)
	
}