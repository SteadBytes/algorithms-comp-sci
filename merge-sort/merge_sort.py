def merge(array, p, q, r):
    """ Merges an array which contains **two sorted subarrays** 
    from [p..q] and [q+1..r] into a fully sorted array

    Args:
        array (array): array containing subarrays
        p (int): Start index
        q (int): Midpoint index between the subarrays
        r (int): End index
    """
    k = p
    i = 0  # lowHalf iterator
    j = 0  # highHalf iterator

    # Copy subarrays out of array so array can be mutated
    lowHalf = array[k:q + 1]
    highHalf = array[q + 1:r + 1]

    while (i < len(lowHalf) and j < len(highHalf)):
        if (lowHalf[i] <= highHalf[j]):
            array[k] = lowHalf[i]
            i += 1
        else:
            array[k] = highHalf[j]
            j += 1
        k += 1

    # Copy remainder of whichever array hasnt been fully copied over yet
    while (i < len(lowHalf)):
        array[k] = lowHalf[i]
        i += 1
        k += 1

    while (j < len(highHalf)):
        array[k] = highHalf[j]
        j += 1
        k += 1


def mergesort(array, p, r):
    """ Sorts an array in place using mergesort

    Args:
        array (array): array to sort
        p (int): start index (0 unless sorting a subarray)
        r (int): end index (len(array)-1 unless sorting a subarray)
    """
    if (p < r):
        q = int((p + r) / 2)
        mergesort(array, p, q)
        mergesort(array, q + 1, r)
        merge(array, p, q, r)


# merge tests
array = [3, 7, 12, 14, 2, 6, 9, 11]
print("Array before merging: %s" % array);
merge(array, 0, int((len(array) - 1) / 2), len(array) - 1)
print("Array after merging: %s" % array);
assert(array == [2, 3, 6, 7, 9, 11, 12, 14])

array = [2, 5, 8, 10, -5, -1, 8, 11]
print("Array before merging: %s" % array);
merge(array, 0, int((len(array) - 1) / 2), len(array) - 1)
print("Array after merging: %s" % array);
assert(array == [-5, -1, 2, 5, 8, 8, 10, 11])

# mergeSort tests
array = [14, 7, 3, 12, 9, 11, 6, 2]
print("Array before sorting: %s" % array);
mergesort(array, 0, len(array) - 1)
print("Array after sorting: %s" % array);
assert(array == [2, 3, 6, 7, 9, 11, 12, 14])

array = [10, -1, 0, 5, -8]
print("Array before sorting: %s" % array);
mergesort(array, 0, len(array) - 1)
print("Array after sorting: %s" % array);
assert(array == [-8, -1, 0, 5, 10])
