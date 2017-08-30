# Selection Sort
**Repeatedly select** the next smallest element and swap it into place.

## Basic Algorithm
```
1. Find the smallest card. Swap it with the first card.
2. Find the second-smallest card. Swap it with the second card.
3. Find the third-smallest card. Swap it with the third card.
4. Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
```

## Minimum Element in a subarray
Each iteration of selection sort requires find the **next-smallest** card to put into the correct location. That item is the **minimum item in the non-sorted subarray**.

Each iteration places another element into its correct place, that means that the remaning unsorted elements form a subarray of length *n-1*, *n-2*, *n-3* etc for each iteration:
```
array = [19, 4, 18, 13, 10]
First swap:
[4, 19, 18, 13, 10] <- 4 is in the correct place
sorted = [4], unsorted = [19, 18, 13, 10]
Second swap:
[4, 10, 18, 13, 19]
sorted = [4, 10], unsorted = [18, 13, 19]
Third swap:
[4, 10, 13, 18, 19]
sorted = [4, 10, 13] unsorted = [18, 19]
Fourth swap:
[4, 10, 13, 18, 19]
sorted = [4, 10, 13, 18] unsorted = [19]
Final:
[4, 10, 13, 18, 19]
sorted = [4, 10, 13, 18, 19] unsorted = []
```
Finding the next-smallest item at each iteration = finding minimum of **unsorted** subarray.

## Analysis
Loop through indices in the array - **O(n)**, then each time:
* Find minimum value -> **O(n)**

    ```python
    def find_minimum(arr):
        """Returns the index of the minimum value in an array
        """
        min_val = arr[0]
        min_index = 0
        for i in range(1, len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
                min_index = i
        return min_index
    ```
    * Finding the minimum value requires looping again over an array -> **O(n)** time.
* Swap into place -> **Constant time**
    *  constant number of instructions (append new item to sorted array).

Therefore the overall running time is **O(n<sup>2</sup>)**