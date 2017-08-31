def insertion_sort(array):
    """ Sort an array into ascending order using insertion sort

    Args:
        array (list): Array/list to sort
    Return:
        Sorted array
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            tmp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = tmp
            j -= 1


array = [22, 11, 99, 88, 9, 7, 42]
print("Array before sorting:  %s" % array);
insertion_sort(array)
print("Array after sorting:  %s" % array);
assert(array == [7, 9, 11, 22, 42, 88, 99])
