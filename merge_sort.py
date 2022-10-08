
def split(arr):
    """
    Divide unsorted list at midpoint into sortedlist
    Returns tow sublist: left and right
    """
    midpoint = len(arr)//2
    return arr[:midpoint], arr[midpoint:]


def merge(left, right):
    """
    Merges 2 arays and sorts them in the process
    """
    sorted_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array


def merge_sort(arr: list):
    """
    Sort List in Ascending

    Returns: New Sorted List

    Divide: Find the midpoints of list and divide into sub lists
    Conquer: Sort sublists recursively

    Combine: Merge all sorted list
    """
    if len(arr) <= 1:
        return arr
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


alist = [34, 56, 34, 23, 34, 3, 31, 23, 354]

print(merge_sort(alist))
