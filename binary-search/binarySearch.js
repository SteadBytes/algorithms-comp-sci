/* */
/**
 * Basic Binary Search Implementation
 * @param {Array} array Array to search through 
 * @param {*} targetValue Item to search for. 
 * @return {number} Index of targetValue in array.
 */
let binarySearch = function (array, targetValue) {
    let min = 0;
    let max = array.length - 1;
    let guess;
    while (max >= min) {
        guess = Math.floor((max + min) / 2);
        if (array[guess] === targetValue) {
            return guess;
        }
        if (array[guess] < targetValue) {
            min = guess + 1;
        } else {
            max = guess - 1;
        }
    }
    return -1;
};

let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
];
console.assert(binarySearch(primes, 73) === 20);
console.assert(doSearch(primes, 100) === -1);
let result = binarySearch(primes, 73);
console.log("Found prime at index " + result);