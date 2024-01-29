import MergeSort
import SelectionSort
import numpy as np
import random


def mergeselectionsort(a, low, high, threshold):
    if low < high:
        if len(a) > threshold:
            mid = (low + high) // 2
            mergeselectionsort(a, low, mid, threshold)
            mergeselectionsort(a, mid + 1, high, threshold)
            MergeSort.merge(a, low, mid, high)
        else:
            SelectionSort.selection_sort(a, len(a)-1)


x = np.random.randint(1, 50, 50)
print('The unsorted array:')
print(x)
threshold = int(input('Enter the threshold:'))
mergeselectionsort(x, 0, len(x)-1, threshold)
print('Sorted array:')
print(x)