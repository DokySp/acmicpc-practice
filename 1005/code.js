// 01:05:51 .56
// 01:18:02 .62 

var fs = require("fs")

var inp = fs.readFileSync('input').toString().split('\n')

// 그래프를 역추적해서 길을 찾기
// 처음부터 길대로 내려오면서 최대 시간값 찾기


var testCase = inp.splice(0,1)[0]

for(var t=0; t<testCase; t++){

    // N, K 입력 받기
    var nodNum = inp.splice(0,1)[0]
    var edgeNum = nodNum.split(' ')[1]
    nodNum = nodNum.split(' ')[0]
    
    var nod = {}
    var tmp = inp.splice(0,1)[0]
    // 건설 시간 입력
    for(var i=0; i<nodNum; i++){
        nod[''+i] = {}
        nod[''+i].time = Number.parseInt(tmp.split(' ')[i])
    }

    // 연결 정보 입력
    for(var i=0; i<edgeNum; i++){
        tmp = inp.splice(0,1)[0]
        if(nod[ ''+(tmp.split(' ')[0]-1) ].to == undefined)
            nod[ ''+(tmp.split(' ')[0]-1) ].to = {length: 0}
        nod[ ''+(tmp.split(' ')[0]-1) ].to[(Number.parseInt(tmp.split(' ')[1])-1)] = (Number.parseInt(tmp.split(' ')[1])-1)
        nod[ ''+(tmp.split(' ')[0]-1) ].to.length++

        if(nod[ ''+(tmp.split(' ')[1]-1) ].from == undefined)
            nod[ ''+(tmp.split(' ')[1]-1) ].from = {length: 0}
        
        nod[ ''+(tmp.split(' ')[1]-1) ].from[(Number.parseInt(tmp.split(' ')[0])-1)] = (Number.parseInt(tmp.split(' ')[0])-1)
        nod[ ''+(tmp.split(' ')[1]-1) ].from.length++

    }

    // 타겟 노드
    var targetNod = inp.splice(0,1)[0]


    // Algorithm

    while(true){

        for(var i=0; i<nodNum; i++){
            // dont have income node
            if(nod[i].from == undefined) {
                console.log(121231233)
                for(var j=0; j<nod[i].to.length; j++){
                    console.log(nod[nod[i].to])
                    
                    nod[nod[i].to[j]].time += nod[i].time
                    nod[nod[i].to[j]][i] = undefined
                }
                console.log(nod)
                console.log()
                return;
                    

            }

        }

    }



}