def binary_search(array, item):
    """Basic iterative binary search implementation.

    Args:
        array (list): List of items to search through.
        item: Target item to search for. 
    Returns:
        (int) Index of item in array.
        - -1 if item not in array.
    """
    min = 0
    max = len(array) - 1
    while (max >= min):
        mid = int((min + max) / 2)
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            min = mid + 1
        else:
            max = mid - 1
    return None


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

assert(binary_search(primes, 73) == 20)
assert(binary_search(primes, 100) == None)

result = binary_search(primes, 73)
print("Found prime at index %s" % result)
