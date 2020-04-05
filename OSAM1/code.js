
var fs = require("fs")

var inp = fs.readFileSync("input").toString()

inp = inp.split('\n')
var avg = 0
var max = -1
var min = 10000

for(var i=0; i<inp.length; i++){
    if( Number.parseInt(inp[i]) > max)
        max =  Number.parseInt(inp[i])

    if( Number.parseInt(inp[i]) < min)
        min =  Number.parseInt(inp[i])

    avg += Number.parseInt(inp[i])
}

avg = avg - min - max

avg = avg / (inp.length-2)

console.log(avg)