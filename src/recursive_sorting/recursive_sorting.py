# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # ** we need make new empty array so we calculate sum
    # ** of both array's length and we make new empty array
    # ** that we are going to fill with the contents of array A and array B
    elements = len(arrA) + len(arrB)  # ** elements is a number
    # ** this is shorthand for making an array of fixed size
    # ** example if we wanted an list of length of 5 we would do [None] * 5 = [None, None, None, None, None]
    merged_arr = [None] * elements
    # ** we now have to fill our new array that we just created
    for i in range(elements):
        # ** if both array A and array B are not empty....
        if len(arrA) > 0 and len(arrB) > 0:
            # ** ....we compare the first items in each list
            # ** and we push up the smallest item to our new array called merged_arr
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:
                merged_arr[i] = arrB.pop(0)
        # ** if only array B is not empty push the first item in array B into our new array
        elif len(arrA) == 0 and len(arrB) > 0:
            merged_arr[i] = arrB.pop(0)
        # ** if only array A is not empty push the first item in array A into our new array
        elif len(arrB) == 0 and len(arrA) > 0:
            merged_arr[i] = arrA.pop(0)
    return merged_arr


# print(merge([4, 5, 7], [2, 6, 7, 8]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # ** base case
    if len(arr) == 1:
        return arr
    # ** split list in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # ** split each list in half again until base case is reached
    left_array = merge_sort(left)
    right_array = merge_sort(right)

    # ** go up the stack and for each list thats been split
    # ** starting from the base case merge left array and right array
    arr = merge(left_array, right_array)
    return arr


print(merge_sort([1, 5, 7, 8, 9, 6, 3, 4, 2, 11, 50, 25, 22, 17]))
# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

# return arr
