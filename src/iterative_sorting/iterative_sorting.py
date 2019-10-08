# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(smallest_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # arr[smallest_index] = arr[i]
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # var = arr[smallest_index]
        # var2 = arr[i]

        # arr[i] = var
        # arr[smallest_index] = var2
        # import pdb; pdb.set_trace()
        print(arr)

        # print("i", "=",i, "j", "=" , j)
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines)

        # TO-DO: swap

    return arr


selection_sort([6, 8, 3, 5, 3, 1])
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
