
var fs = require("fs")

// var inp = fs.readFileSync("./input").toString().split("\n")
var inp = fs.readFileSync("/dev/stdin").toString().split("\n")

const testCase = inp[0]

for(var i=0; i<testCase; i++){

    var m1 = inp[i+1].split(' ')
    var m2 = {x: Number.parseInt(m1[3]), y: Number.parseInt(m1[4]), r: Number.parseInt(m1[5])}
    m1 = {x: Number.parseInt(m1[0]), y: Number.parseInt(m1[1]), r: Number.parseInt(m1[2])}

    var distance = Math.sqrt(((m2.x-m1.x)*(m2.x-m1.x) + (m2.y-m1.y)*(m2.y-m1.y)))

    // console.log(m1.r, m2.r, distance)

    var maxLen = Math.max(m1.r, m2.r, distance)

    if(  (m1.r+m2.r+distance)/maxLen > 2  ){
        console.log(2)
    } else if( (m1.r+m2.r+distance)/maxLen == 2 ){
        if(distance == 0)
            console.log(-1)
        else
            console.log(1)
    } else if( (m1.r+m2.r+distance)/maxLen < 2 ) {
        console.log(0)
    }

    // console.log()


}
