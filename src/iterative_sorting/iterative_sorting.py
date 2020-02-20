# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    indexing_length = range(0, len(arr) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j

        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]

    return arr


print(selection_sort([5, 43, 456, 1, 6, 6757, 32, 87, 98]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    indexing_length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


print(bubble_sort([4, 6, 8, 7, 24, 54, 87, 98, 5, 3]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
