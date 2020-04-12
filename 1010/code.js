//  31:11 .63 
var inp = require('fs').readFileSync('input').toString().split('\n')

var tc = inp[0]-0

for(var T=1; T<=tc; T++){

    var tmp = inp[T].split(' ')

    var n = tmp[0]-0
    var m = tmp[1]-0
    var path = []

    var queue = []

    for(var i=0; i<n; i++){
        var tmp = []
        for(var j=0; j<m; j++)
            tmp.push(0)
        path.push(tmp)
    }

    var i=0
    var j=0
    for(V=0; V<4; V++){
        if(path[i+1] != undefined){  // check right-bottom area
            queue[queue.length] = j
            path[i][j] += 1
            i++
            j++
        } else if(path[i+1] == undefined){  // reach the bottom of array
            for(var a=queue[queue.length-1]+1; a<m; a++){
                path[i][j++] += 1
            }
            queue.push(queue.pop()+1)
        }
        console.log(path)
        console.log(queue)
        console.log()
    }

}