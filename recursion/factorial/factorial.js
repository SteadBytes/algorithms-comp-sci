let iterativeFactorial = function (n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
};

let recursiveFactorial = function (n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
};

console.log("The value of 0! is " + factorial(0) + ".");
console.log("The value of 5! is " + factorial(5) + ".");

console.assert(recursiveFactorial(0) === 1);
console.assert(recursiveFactorial(5) === 120);
console.assert(recursiveFactorial(2) === 2);
console.assert(recursiveFactorial(6) === 720);

console.assert(iterativeFactorial(5) === 120);
console.assert(iterativeFactorial(0) === 1);
console.assert(iterativeFactorial(2) === 2);
console.assert(iterativeFactorial(6) === 720);