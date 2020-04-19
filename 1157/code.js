
// var inp = require('fs').readFileSync('input').toString()
var inp = require('fs').readFileSync('/dev/stdin').toString()

var len = inp.length
inp = inp.toUpperCase()
var max = -1
var maxAlpha = -1
var alpha = []

for(var i=0; i<26; i++)
    alpha[i] = 0

for(var i=0; i<len; i++)
    alpha[inp.charCodeAt(i)-65]++

for(var i=0; i<26; i++)
    if(alpha[i] > max){
        max = alpha[i]
        maxAlpha = i
    }

for(var i=0; i<26; i++)
    if(max == alpha[i] && maxAlpha != i)
        maxAlpha = -1

if(maxAlpha == -1)
    console.log('?')
else
    console.log(String.fromCharCode(maxAlpha+65))