var fs = require("fs")

var inp = fs.readFileSync("/dev/stdin").toString().split("\n")
// var inp = fs.readFileSync("./input").toString().split("\n")

// var ts = inp.splice(0,1)[0]
var ts = inp[0]
// splice 함수를 제거 -> 영향이 크다... 안쓰는 것이 좋다!

// 모든 변수 전역변수화 -> 지역변수일 때가 시간 효율이 더 좋다! (미미하긴 함)
// var a
// var b
var res = "";

for(var T=1; T<=ts; T++){
	// split 함수 사용 최소화 -> 어느 정도 의미있는 영향을 준다!
	// a = inp.splice(0,1)[0]
	// b = a.split(" ")[1]-0
	// a = a.split(" ")[0]-0
	var a = inp[T].split(' ')

	// console.log 대신 데이터를 모두 모아 출력 -> 콘솔로그가 시간 많이 갉아먹음! (매우 효과적!)
	// console.log(res)
	res += (a[0]-0) + (a[1]-0)+'\n'
}

console.log(res)