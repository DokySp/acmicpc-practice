// 01:05:51 .56
// 01:07:52 .06 (제출 => 시간초과)

var fs = require("fs")

// var inp = fs.readFileSync('/dev/stdin').toString().split('\n')
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
        nod[''+i].to = []
        nod[''+i].from = 0
        nod[''+i].timeTmp = []
    }
    nod.length = nodNum
    
    // 연결 정보 입력
    for(var i=0; i<edgeNum; i++){
        tmp = inp.splice(0,1)[0]
        nod[ tmp.split(' ')[0]-1 ].to.push(tmp.split(' ')[1]-1)
        nod[ tmp.split(' ')[1]-1 ].from += 1
    }

    // 타겟 노드
    var targetNod = inp.splice(0,1)[0]-1

    console.log(nod)
    console.log()

    // 위상정렬
    while(true){

        if(nod[targetNod].from == 0){
            console.log(nod[targetNod].time)
            break;
        }

        var endNods = []

        // from[].length == 0 인 노드를 찾기
        for(var i = 0 ; i < nodNum; i++){
            if( nod[i] != undefined && nod[i].from == 0 ){
                
                // 1. 부모의 time값을 자식의 timeTmp로 넘김
                // 2. 부모에 연결된 자식의 from := false
                //   2-1. 들어오는 노드가 여러개일 경우, 전부 지어야 하므로 들어오는 노드 값을 카운트해야 함!
                // 3. 부모 노드를 delete (★delete 연산자 사용)
                for(var c=0; c<nod[i].to.length; c++){
                    nod[nod[i].to[c]].timeTmp.push(nod[i].time)
                    endNods.push(nod[i].to[c])
                }
                delete nod[i]
                nod.length--
                
            }

        }

        for(c=0; c<endNods.length; c++)
            if(nod[endNods[c]] != undefined)
                nod[endNods[c]].from -= 1
        
        // 4. timeTmp에 들어있는 값 중 최댓값을 time에 더함
        //   4-1. from이 0이 아닌 경우, time을 더하지 않음! (동시 건설 불가능)
        // 5. timeTmp = []

        for(var i = 0 ; i < nodNum; i++){

            if( nod[i] != undefined && nod[i].timeTmp.length != 0){
                if(nod[i].from == 0){
                    nod[i].timeTmp.sort()
                    var max = nod[i].timeTmp[ nod[i].timeTmp.length-1 ]
                    nod[i].time += max
                }
                nod[i].timeTmp = []
            }
        }

        console.log(nod.length)
    
    }

}