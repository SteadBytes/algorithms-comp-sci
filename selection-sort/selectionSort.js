/**
 * Swaps two items position in an array.
 * @param {array} array array to mutate 
 * @param {number} firstIndex Index of first item to swap.
 * @param {number} secondIndex Index of second item to swap.
 */
let swap = function (array, firstIndex, secondIndex) {
    let tmp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = tmp;
};

/**
 * Finds the index of the minimum value in a subarray.
 * @param {array} array entire array containing the subarray
 * @param {number} startIndex Index at which subarray begins
 * @returns {number} Index of minimum value within subarray
 */
let indexOfMinimum = function (array, startIndex) {

    let minValue = array[startIndex];
    let minIndex = startIndex;

    for (let i = minIndex + 1; i < array.length; i++) {
        if (array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    }
    return minIndex;
};

/**
 * Sort an array into ascending order using selection sort.
 * @param {array} array array to sort 
 */
let selectionSort = function (array) {
    let min;
    for (let i = 0; i < array.length; i++) {
        // Get index of min value from unsorted subarray
        min = indexOfMinimum(array, i);
        // Swap into correct place
        swap(array, i, min);
    }
};

let array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

let array = [-3, 10, -8, 11];
selectionSort(array);
Program.assertEqual(array, [-8, -3, 10, 11]);