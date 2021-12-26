# K-sort task

array_length = int(input())
arr = list(map(int, input().split()))
k_param = int(input())

"""
def k_sort2(array, k):
    permutations = 0
    for idx in range(len(array) - k):
        if array[idx] > array[idx + k]:
            array[idx], array[idx + k] = array[idx + k], array[idx]
            permutations += 1

    if array == sorted(array):
        return permutations
    return -1
"""

def k_sort(array, k, length):
    permutations = 0

    #  This loop is to sort k subarays
    for k_th_array in range(k + 1):
        changed = True

        while changed:
            changed = False
            for inner in range(k_th_array, length, k):
                successor = inner + k
                if successor < length:
                    if array[inner] > array[successor]:
                        array[inner], array[successor] = array[successor], array[inner]
                        permutations += 1
                        changed = True

    if array == sorted(array):
        return permutations
    return -1


print(k_sort(arr, k_param, array_length))
