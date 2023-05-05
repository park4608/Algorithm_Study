let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [n, m] = input[0].split(' ').map((e) => parseInt(e));
let setA = input[1]
  .split(' ')
  .map((e) => parseInt(e))
  .sort(function (a, b) {
    return a - b;
  });
let setB = input[2]
  .split(' ')
  .map((e) => parseInt(e))
  .sort(function (a, b) {
    return a - b;
  });

let ans = [];

function binarySearch(arr, target) {
  let s = 0;
  let e = arr.length - 1;

  while (s <= e) {
    const m = Math.floor((s + e) / 2);

    if (arr[m] === target) {
      return m;
    } else if (arr[m] < target) {
      s = m + 1;
    } else {
      e = m - 1;
    }
  }
  return -1;
}

for (let i = 0; i < setA.length; i++) {
  let bs = binarySearch(setB, setA[i]);
  if (bs === -1) {
    ans.push(setA[i]);
  }
}

if (ans.length !== 0) {
  console.log(ans.length);
  console.log(ans.join(' '));
} else {
  console.log(0);
}
