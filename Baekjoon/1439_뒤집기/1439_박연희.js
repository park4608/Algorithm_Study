let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let strZero = input[0].split('1').filter((e) => e !== '');
let strOne = input[0].split('0').filter((e) => e !== '');
console.log(strZero.length > strOne.length ? strOne.length : strZero.length);
