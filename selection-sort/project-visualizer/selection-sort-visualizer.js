void setup() {
    size(1000, 1000);
    frameRate(0.1);
    draw()
}

void draw() {
    background(255)
    let array = Array.from({
        length: 10
    }, () => Math.floor(Math.random() * 1000));
    selectionSort(array);
}

let xStart = 100;
let itemWidth = 50; // TODO scale up for array item size i.e. 1000000 wont fit.
let yStart = 50;
let arrayHeight = 50;
let fontSize = 12;

/**
 * Draws a visualization of the current step in
 * selection sort
 * @param {array} array array to display 
 * @param {number} y y-coord to draw current array
 * @param {number} minIndex Index of current minimum item
 * @param {number} currentIndex Index of current item in sort loop
 */
let displayArray = function (array, y, minIndex, currentIndex) {
    textFont(createFont("monospace"), 12);
    for (let i = 0; i < array.length; i++) {
        if (i === minIndex) {
            fill(0, 26, 255); // Blue shows item to be swapped
        } else {
            fill(0, 0, 0);
        }
        text(array[i], xStart + (itemWidth * i), y);
    }
    if (currentIndex >= 0) {
        // Default browser line-height = 1.2, multiply by font-size
        // to get coord of top of character
        line(xStart + (minIndex + 0.25) * itemWidth, y + (fontSize * 1.2 / 4),
            xStart + (currentIndex + 0.25) * itemWidth, y + arrayHeight - (fontSize * 1.2));
    }
};

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


// var array = [444, 444, 100, 888, 136];