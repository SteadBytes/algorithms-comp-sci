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


def selection_sort(arr):
    """Sort an array in ascending order using selection sort.

    Uses arr.pop to produce unsorted subarray instead of tracking index of
    sorted items.
    """
    sorted_arr = []
    for i in range(len(arr)):
        min_index = find_minimum(arr)
        sorted_arr.append(arr.pop(min_index))
    return sorted_arr


array = [22, 11, 99, 88, 9, 7, 42]
print("Unsorted = %s" % array)
array = selection_sort(array)
assert(array == [7, 9, 11, 22, 42, 88, 99])
print("Sorted = %s" % array)

array = [-3, 10, -8, 11]
print("Unsorted = %s" % array)
array = selection_sort(array)
assert(array == [-8, -3, 10, 11])
print("Sorted = %s" % array)
