
var fs = require('fs')

var inp = fs.readFileSync('/dev/stdin').toString().split('\n')
// var inp = fs.readFileSync('./input').toString().split('\n')

var testCase = inp[0]


for(var i=0; i<testCase; i++){

  var ff = inp[i+1]

  console.log(fib(ff==0 ? 1: ff-1), fib(ff))

}

//    0 1 2 3 4
// 5  0 1 1 2 3 5 8
function fib(n){

  var n1 = 0
  var n2 = 1
  var res = 0

  if(n == 0)
    return 0
  else if(n == 1)
    return 1
  
  for(var m=2; m <= n; m++){
    res = n1+n2
    n1 = n2
    n2 = res
  }
  return res

}

