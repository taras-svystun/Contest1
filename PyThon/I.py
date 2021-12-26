# K minimum sums

k = int(input())
k_arrays = list()
for _ in range(k):
    array = list(map(int, input().split()))
    k_arrays.append(array)

def smallest_sums(length: int, arrays: list) -> int:
    sorted_arrays = list()
    sums = list()
    for array in arrays:
        sorted_arrays.append(sorted(array))

    return sorted_arrays


print(smallest_sums(k, k_arrays))