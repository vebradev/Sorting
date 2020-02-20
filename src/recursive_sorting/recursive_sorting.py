# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    merged_arr = []
    left_element = 0
    right_element = 0
    while left_element < len(arrA) and right_element < len(arrB):
        if arrA[left_element] < arrB[right_element]:
            merged_arr.append(arrA[left_element])
            left_element += 1
        else:
            merged_arr.append(arrB[right_element])
            right_element += 1

    return merged_arr + arrA[left_element:] + arrB[right_element:]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # divide & conquer
        mid = len(arr) // 2
        lhs = merge_sort(arr[:mid])
        rhs = merge_sort(arr[mid:])
        return merge(lhs, rhs)
    return arr

print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
