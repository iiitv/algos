function fibonacci(num, memo) {
  memo = memo || {1:0, 2:1};

  if (memo[num] || memo[num] === 0)
    return memo[num];

  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}

function main() {
  console.log("result => " + fibonacci(5));
  // result => 3
  console.log("result => " + fibonacci(12));
  // result => 89
  console.log("result => " + fibonacci(50));
  // result => 7778742049
}

main();
