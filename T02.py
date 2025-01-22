from heapq import merge
import math

# We define c=1
c = 1
def merge_two_arrays(arr1, arr2):
    merged = list(merge(arr1, arr2))
    return merged, c*(len(merged))

def merge_k_sorted_arrays(arrays):

    k = len(arrays)
    
    # Base Case
    if k == 1:
        return arrays[0], len(arrays[0])
    
    # Recursive Case
    raise NotImplementedError

# k = 4 sorted arrays, each of size n = 3
arrays = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]
k = len(arrays)
n = len(arrays[0])

result, ops = merge_k_sorted_arrays(arrays)
print("Merged array:", result)
print("Number of operations (count):", ops)
print("Number of operations (theory):", c*k*n*(1 + math.log2(k)))