def swap(array, ind1, ind2):
    """ Swaps two items in an array - mutates original array.

    Args:
        array (array): array to mutate
        ind1 (int): index of first item to swap
        ind2 (int): index of second item to swap
    """
    tmp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = tmp


def partition(array, p, r):
    """Partitions an array using rightmost element as pivot

    Args:
        array (array): array to partition
        p (int): start index
        r (int): end index
    Returns
        (int) final index  of pivot
    """
    q = p
    for j in range(p, r):
        if array[j] <= array[r]:  # use last element as pivot
            swap(array, j, q)
            q += 1
    swap(array, q, r)
    return q


def quicksort(array, p, r):
    """Sort an array (ascending) using quicksort

    Args:
        array (array): array to sort
        p (int): start index
        r (int): end index
    """
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


def pythonic_quicksort(array):
    """ Sort an array (ascending) using quicksort.

    Uses python built in features such as list comprehension and slicing

    Args:
        array (array): array to sort
    Returns:
        (array) sorted array
    """
    if len(array) < 2:
        return array  # base case
    else:
        pivot = array[0]
        low_half = [i for i in array[1:] if i <= pivot]
        high_half = [i for i in array[1:] if i > pivot]

        return pythonic_quicksort(low_half) + [pivot] + pythonic_quicksort(high_half)

# Tests -------------------------------------------


# Partition Tests
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6]
print("Array before partitioning: %s" % array)
q = partition(array, 0, len(array) - 1)
print("Array after partitioning: %s" % array)
assert(q == 4)
assert(array == [5, 2, 3, 4, 6, 7, 14, 9, 10, 11, 12])

array = [9, -5, 5, 11, 6, 2, 14, 3, 0, 4, 6]
print("Array before partitioning: %s" % array)
q = partition(array, 0, len(array) - 1)
print("Array after partitioning: %s" % array)
assert(q == 7)
assert(array == [-5, 5, 6, 2, 3, 0, 4, 6, 11, 14, 9])

# Quicksort tests
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
print("Array before sorting: %s" % array)
quicksort(array, 0, len(array) - 1)
print("Array after sorting: %s" % array)
assert(array == [2, 3, 5, 6, 7, 9, 10, 11, 12, 14])

array = [9, -7, -5, 11, 12, 2, 14, 3, 10, 6]
print("Array before sorting: %s" % array)
quicksort(array, 0, len(array) - 1)
print("Array after sorting: %s" % array)
assert(array == [-7, -5, 2, 3, 6, 9, 10, 11, 12, 14])
