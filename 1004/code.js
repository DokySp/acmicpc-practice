
var fs = require('fs')

var inp = fs.readFileSync('/dev/stdin').toString().split('\n')
// var inp = fs.readFileSync('input').toString().split('\n')

const testCase = Number.parseInt(inp.splice(0,1)[0])

for(var i=0; i<testCase; i++){

    var point = inp.splice(0,1)[0].split(' ')
    const stPoint = {x: Number.parseInt(point[0]), y: Number.parseInt(point[1])}
    const endPoint = {x: Number.parseInt(point[2]), y: Number.parseInt(point[3])}
    
    const astNum = inp.splice(0,1)[0]
    var ast = []
    for(var a=0; a<astNum; a++){
        var astPoint = inp.splice(0,1)[0].split(' ')
        ast.push({x: Number.parseInt(astPoint[0]), y: Number.parseInt(astPoint[1]), r: Number.parseInt(astPoint[2])})
    }

    // algorithm
    // 출발/도착 지점과 원 중심 거리 < 반지름 길이
    // -> 해당 항성계에 포함!
    
    var bypath = 0
    var sameArea = false

    for(var c=0; c<ast.length; c++){
        if ( ast[c].r > Math.sqrt( (ast[c].x-stPoint.x)*(ast[c].x-stPoint.x) + (ast[c].y-stPoint.y)*(ast[c].y-stPoint.y) ) ){
            bypath++
            sameArea = true
        }
        if ( ast[c].r > Math.sqrt( (ast[c].x-endPoint.x)*(ast[c].x-endPoint.x) + (ast[c].y-endPoint.y)*(ast[c].y-endPoint.y) ) ){
            if(sameArea)
                bypath--
            else
                bypath++
        }
        sameArea = false
    }
    console.log(bypath)
}

