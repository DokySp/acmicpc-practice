// 01:05:51 .56

var fs = require("fs")

var inp = fs.readFileSync('input').toString().split('\n')

// 그래프를 역추적해서 길을 찾기
// 처음부터 길대로 내려오면서 최대 시간값 찾기


var testCase = inp.splice(0,1)[0]

for(var t=0; t<testCase; t++){

    // N, K 입력 받기
    var buildingN = inp.splice(0,1)[0]
    var edgeRuleN = buildingN.split(' ')[1]
    buildingN = buildingN.split(' ')[0]
    
    var nod = {}
    var tmp = inp.splice(0,1)[0]
    // 건설 시간 입력
    for(var i=1; i<=buildingN; i++){
        nod['n'+i] = {}
        nod['n'+i].time = tmp.split(' ')[i]
    }
    
    // 연결 정보 입력
    for(var i=1; i<=edgeRuleN; i++){
        tmp = inp.splice(0,1)[0]
        if(nod[ 'n'+tmp.split(' ')[0] ].to == undefined)
            nod[ 'n'+tmp.split(' ')[0]].to = []
        nod[ 'n'+tmp.split(' ')[0] ].to.push(tmp.split(' ')[1])
        
        if(nod[ 'n'+tmp.split(' ')[1] ].from == undefined)
            nod[ 'n'+tmp.split(' ')[1]].from = []
        
        nod[ 'n'+tmp.split(' ')[1] ].from.push(tmp.split(' ')[0])
        
    }

    // 타겟 노드
    var targetNod = inp.splice(0,1)[0]

    


    console.log(findRoad(targetNod))



}