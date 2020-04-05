
var fs = require("fs")

var inp = fs.readFileSync("input").toString()

inp = inp.split('\n')

var testCase = inp.splice(0,1)[0]
var table = []

for(var i=0; i<testCase; i++){
    var item = Number.parseInt( inp.splice(0,1)[0] )
    if(table[item] == undefined){
        table[item] = 1
    } else {
        table[item] += 1
    }
}

var res = ""
for(var i=0; i<table.length; i++){
    if(table[i] == 1)
        res += i + " "
}
res = res.slice(0,res.length-1)
console.log(res)