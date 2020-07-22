# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    merged = []

    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        merged += arrB
    else:
        merged += arrA
    return merged


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

