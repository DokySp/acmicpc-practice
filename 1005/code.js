// 01:05:51 .56
// 01:18:02 .62 
// 01:07:52 .06 (제출 => 시간초과)

var fs = require("fs")

// var inp = fs.readFileSync('/dev/stdin').toString().split('\n')
var inp = fs.readFileSync('input').toString().split('\n')

// 그래프를 역추적해서 길을 찾기
// 처음부터 길대로 내려오면서 최대 시간값 찾기


var testCase = inp.splice(0,1)[0]

for(var t=0; t<testCase; t++){

    var start = Date.now()

    // N, K 입력 받기
    var nodNum = inp.splice(0,1)[0]
    var edgeNum = nodNum.split(' ')[1]
    nodNum = nodNum.split(' ')[0]
    
    var nod = {}
    var tmp = inp.splice(0,1)[0]

    // 건설 시간 입력
    for(var i=0; i<nodNum; i++){
        nod[i] = {}
        nod[i].time = tmp.split(' ')[i] - 0
        nod[i].to = []
        nod[i].from = 0
        nod[i].timeTmp = []
    }
    
    // 연결 정보 입력
    for(var i=0; i<edgeNum; i++){
        tmp = inp.splice(0,1)[0]
        nod[ tmp.split(' ')[0]-1 ].to.push(tmp.split(' ')[1]-1)
        nod[ tmp.split(' ')[1]-1 ].from += 1
    }

    // 타겟 노드
    var targetNod = inp.splice(0,1)[0]-1
    var endQueue = []


    // 위상정렬
    
    // 인디그리 0인 노드 찾기
    for(var i = 0; i < nodNum; i++){
        if(nod[i].from == 0)
            endQueue.push(i)
    }
    console.log(nod)
    
    while(true){



        var trig = endQueue.splice(0,1)[0]
        // nod[trig].to
        console.log(trig)



        // ending conditions
        if(nod[targetNod].from == 0){
            console.log(nod[trig].time)
            break;
        }

	    // 자식 노드로 시간값을 보냄 & from--
        for(var a=0; a<nod[trig].to.length; a++){
            nod[ nod[trig].to[a] ].timeTmp.push( nod[trig].time )
            nod[ nod[trig].to[a] ].from--
            
            // 자식 노드를 큐에 추가
            endQueue.push( nod[trig].to[a] )
        }

        // from 노드가 0일 경우, timeTmp 최댓값을 time에 추가
        if(nod[trig].from == 0 && nod[trig].timeTmp.length != 0){
            nod[trig].time += nod[trig].timeTmp.sort()[nod[trig].timeTmp.length-1]
            nod[trig].timeTmp = []
        }
        


        console.log(endQueue)
        console.log(nod)
        console.log()
        

    }


}
