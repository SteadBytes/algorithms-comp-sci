/**
 * Inserts a value into a sorted sub array at its correct location.
 * @param {array} array Array to mutate 
 * @param {*} rightIndex Index of last element in sorted subarray
 * @param {*} value Value to insert into sorted subarray
 */
let insert = function (array, rightIndex, value) {
    for (let i = rightIndex; i >= 0 && array[i] > value; i--) {
        array[i + 1] = array[i];
    }
    array[i + 1] = value;
};

/**
 * Sorts an  array in ascending order using Insertion Sort
 * @param {*} array array to sort
 */
let insertionSort = function (array) {
    for (let i = 1; i < array.length; i++) {
        insert(array, i - 1, array[i]);
    }
};
/**
 * Compares contents and order of simple, 1d arrays
 * @param {array} arr1 
 * @param {array} arr2 
 * @return {bool} Whether arrays are equal
 */
let arrayAreEqual = function (arr1, arr2) {
    return arr1.lenth === arr2.lenth && arr1.reduce((a, b, i) => a && arr1[i] === arr2[i], true)
}

let array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
console.log("Array after sorting:  " + array);
console.assert(true === arrayAreEqual(array, [7, 9, 11, 22, 42, 88, 99]));

let array = [22, -5, 11, -20, 55, 3, 22];
insertionSort(array);
console.log("Array after sorting:  " + array);
console.assert(true === arrayAreEqual(array, [-20, -5, 3, 11, 22, 22, 55]));