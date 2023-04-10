let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let n = parseInt(input[0]);
let rope = input
  .slice(1)
  .map((e) => parseInt(e))
  .sort((a, b) => {
    return a - b;
  });
let maxW = rope[n - 1];
for (let i = n - 2; i >= 0; i--) {
  if (rope[i] * (n - i) > maxW) {
    maxW = rope[i] * (n - i);
  }
}
console.log(maxW);
