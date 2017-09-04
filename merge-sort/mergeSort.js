/**
 * Merges an array which contains two sorted subarrays from [p..q] and [q+1..r]
 * @param {array} array array with subarrays to merge
 * @param {int} p start index 
 * @param {int} q mid-index between the subarrys 
 * @param {int} r end index 
 */
let merge = function (array, p, q, r) {
    let lowHalf = [];
    let highHalf = [];

    let k = p;
    let i;
    let j;

    // Copy subarrays to allow mutation of original array
    for (i = 0; k <= q; i++, k++) {
        lowHalf[i] = array[k];
    }
    for (j = 0; k <= r; j++, k++) {
        highHalf[j] = array[k];
    }

    k = p;
    i = 0;
    j = 0;

    // Repeatedly compare the lowest untaken element in
    //  lowHalf with the lowest untaken element in highHalf
    //  and copy the lower of the two back into array
    while (i < lowHalf.length && j < highHalf.length) {
        if (lowHalf[i] <= highHalf[j]) {
            array[k] = lowHalf[i];
            i++;
        } else {
            array[k] = highHalf[j];
            j++;
        }
        k++;
    }
    // Copy remaining elements from array which 
    // has not been fully copied
    while (i < lowHalf.length) {
        array[k] = lowHalf[i];
        i++;
        k++;
    }

    while (j < highHalf.length) {
        array[k] = highHalf[j];
        j++;
        k++;
    }
};

/**
 * Recursively Merge sorts an array
 * @param {array} array Array to sort 
 * @param {int} p  beginning index
 * @param {*} r end index
 */
let mergeSort = function (array, p, r) {
    if (p < r) {
        let q = Math.floor((p + r) / 2);
        mergeSort(array, p, q);
        mergeSort(array, q + 1, r);
        merge(array, p, q, r);
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

// merge tests
let array = [3, 7, 12, 14, 2, 6, 9, 11];
console.log("Array before merging: " + array);
merge(array, 0,
    Math.floor((0 + array.length - 1) / 2),
    array.length - 1);
console.log("Array after merging: " + array);
console.assert(true === arrayAreEqual(array, [2, 3, 6, 7, 9, 11, 12, 14]));

array = [2, 5, 8, 10, -5, -1, 8, 11];
console.log("Array before merging: " + array);
merge(array, 0,
    Math.floor((0 + array.length - 1) / 2),
    array.length - 1);
console.log("Array after merging: " + array);
console.assert(true === arrayAreEqual(array, [-5, -1, 2, 5, 8, 8, 10, 11]));

// mergeSort tests
array = [14, 7, 3, 12, 9, 11, 6, 2];
console.log("Array before sorting: " + array);
mergeSort(array, 0, array.length - 1);
console.log("Array after sorting: " + array);
console.assert(true === arrayAreEqual(array, [2, 3, 6, 7, 9, 11, 12, 14]));

array = [10, -1, 0, 5, -8];
console.log("Array before sorting: " + array);
mergeSort(array, 0, array.length - 1);
console.log("Array after sorting: " + array);
console.assert(true === arrayAreEqual(array, [-8, -1, 0, 5, 10]));