import QuickSort
import numpy as np


def search(a, left, right, k):
        if k < len(a)+1  and k > 0:
            pivot_index = QuickSort.partition(a, left, right)
            if pivot_index == k-1:
                return a[pivot_index]
            elif pivot_index < k-1:
                return search(a, pivot_index + 1, right, k)
            elif pivot_index > k-1:
                return search(a, left, pivot_index, k)
            else:
                return -1


x = np.random.randint(1, 50, 50)
print('The unsorted array:')
print(x)
n = len(x)
k = int(input('Enter the value of k:\n'))
e = search(x, 0, n-1, k)
print('The '+str(k)+'th smallest element:')
print(e)