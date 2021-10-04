function fibonacci(p) {
    if(p === 1 || p === 2) {
        return p-1; // base case
    } else {

        let a = 0;
        let b = 1;
        // 0 1 1 2 3 5 8 ...
        let fib = 0;
        for(var i = 2 ; i < p ; i = i + 1) {
            fib = a + b;
            a = b;
            b = fib;
        }

        return fib;
    }
}

function main() {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
      });
      
    readline.question("Enter value of n ", n => {
        console.log(fibonacci(n));
        readline.close()
      });    
}

main();
  

