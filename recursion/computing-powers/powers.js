function isEven(n) {
    return n % 2 === 0;
};

function isOdd(n) {
    return !isEven(n);
};

function power(x, n) {
    console.log("Computing " + x + " raised to power " + n + ".");
    // base case
    if (n === 0) {
        return 1;
    }
    // recursive case: n is negative
    if (n < 0) {
        return 1 / power(x, -n);
    }
    // recursive case: n is odd
    if (isOdd(n)) {
        return x * power(x, n - 1);
    }
    // recursive case: n is even
    if (isEven(n)) {
        let y = power(x, n / 2);
        return y * y;
    }
};

function displayPower(x, n) {
    console.log(x + " to the " + n + " is " + power(x, n));
};

displayPower(3, 0);
console.assert(power(3, 0) === 1);
displayPower(3, 1);
console.assert(power(3, 1) === 3);
displayPower(3, 2);
console.assert(power(3, 2) === 9);
displayPower(3, -1);
console.assert(power(3, -1) === 1 / 3);
displayPower(2, 6);
console.assert(power(2, 6) === 64);
displayPower(2, 6);
console.assert(power(2, -6) === 1 / 64);