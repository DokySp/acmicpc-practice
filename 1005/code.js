// 01:05:51 .56
// 01:18:02 .62 
// 01:07:52 .06 (제출 => 시간초과)

var fs = require("fs")

var inp = fs.readFileSync('/dev/stdin').toString().split('\n')
// var inp = fs.readFileSync('input').toString().split('\n')

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
        nod[i].time = tmp.split(' ')[i]-0
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

    // 큐에 인디그리 0인 노드 삽입
    var queue = []
    for(var i=0; i<nodNum; i++)
        if(nod[i].from == 0)
            queue.push(i)

    // 위상정렬
    
    // 인디그리 0인 노드 찾기
    for(var i = 0; i < nodNum; i++){
        if(nod[i].from == 0)
            endQueue.push(i)
    }
    console.log(nod)
    
    while(true){

        // 1.
        var trig = queue.splice(0,1)[0]

        // 2.
        if(nod[trig].from == 0 && nod[trig].timeTmp.length != 0)
            nod[trig].time += nod[trig].timeTmp.sort()[ nod[trig].timeTmp.length-1 ]

        // 3.
        if(trig == targetNod && nod[trig].from == 0){
            console.log(nod[trig].time)
            break;
        }

        for(var c=0; c<nod[trig].to.length; c++){
            // 4.
            nod[ nod[trig].to[c] ].timeTmp.push(nod[trig].time)
            // 5.
            nod[ nod[trig].to[c] ].from--

            if(nod[ nod[trig].to[c] ].from == 0)
                queue.push(nod[trig].to[c])
        }
    }
}
