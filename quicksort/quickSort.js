// 
/**
 * Swaps two items in an array, mutates the original array
 * @param {array} array array to mutate
 * @param {number} i1 index of first item to swap
 * @param {number} i2 index of second item to swap
 */
let swap = function (array, i1, i2) {
    let tmp = array[i1];
    array[i1] = array[i2];
    array[i2] = tmp;
};
/**
 * Partitions an array using rightmost element as pivot.
 * @param {array} array array to partition
 * @param {number} p starting index
 * @param {number} r ending index (also pivot)
 * @return {number} final index of pivot
 */
let partition = function (array, p, r) {
    let q = p;
    // Compare array[j] with array[r], for j = p, p+1,...r-1
    //  array[p..q-1] are values known to be <= to array[r]
    //  array[q..j-1] are values known to be > array[r]
    //  array[j..r-1] haven't been compared with array[r]
    for (let j = p; j < r; j++) {
        if (array[j] <= array[r]) {
            swap(array, j, q);
            q++;
        }
    }
    swap(array, q, r);
    return q;
};
/**
 * Sort an array (ascending) using quicksort
 * @param {array} array array to sort
 * @param {number} p start index 
 * @param {number} r end index
 */
let quickSort = function (array, p, r) {
    if (p < r) {
        let q = partition(array, p, r);
        quickSort(array, p, q - 1);
        quickSort(array, q + 1, r);
    }
};

// Testing ----------------------------------------------

/**
 * Compares contents and order of simple, 1d arrays
 * @param {array} arr1 
 * @param {array} arr2 
 * @return {boolean} Whether arrays are equal
 */
let arrayAreEqual = function (arr1, arr2) {
    return arr1.lenth === arr2.lenth && arr1.reduce((a, b, i) => a && arr1[i] === arr2[i], true)
}

// Partition Tests
let array, q;
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6];
console.log("Array before partitioning: " + array);
q = partition(array, 0, array.length - 1);
console.log("Array after partitioning: " + array);
console.assert(q === 4);
console.assert(true === arrayAreEqual(array, [5, 2, 3, 4, 6, 7, 14, 9, 10, 11, 12]));

array = [9, -5, 5, 11, 6, 2, 14, 3, 0, 4, 6];
console.log("Array before partitioning: " + array);
q = partition(array, 0, array.length - 1);
console.log("Array after partitioning: " + array);
console.assert(q, 7);
console.assert(true === arrayAreEqual(array, [-5, 5, 6, 2, 3, 0, 4, 6, 11, 14, 9]));

// Quicksort tests
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
console.log("Array before sorting: " + array);
quickSort(array, 0, array.length - 1);
console.log("Array after sorting: " + array);
console.assert(true === arrayAreEqual(array, [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]));

array = [9, -7, -5, 11, 12, 2, 14, 3, 10, 6];
console.log("Array before sorting: " + array);
quickSort(array, 0, array.length - 1);
console.log("Array after sorting: " + array);
console.assert(true === arrayAreEqual(array, [-7, -5, 2, 3, 6, 9, 10, 11, 12, 14]));