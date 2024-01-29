import time
import numpy as np
import SelectionSort
import InsertionSort
import HeapSort
import MergeSort
import QuickSort

# testing each sort
x = [4, 5, 3, 7, 1, 9, 10, 6, 4, 3]
print('unsorted array:')
print(x)
q = x
QuickSort.QuickSort(q, 0, len(q))
print('sorted array by quick sort:')
print(q)
m = x
MergeSort.mergesort(m, 0, len(m) - 1)
print('sorted array by merge sort:')
print(m)
h = x
HeapSort.heapSort(h)
print('sorted array by quick sort:')
print(h)
s = x
SelectionSort.selection_sort(s, len(s))
print('sorted array by selection sort:')
print(s)
i = x
InsertionSort.insertionsort(i, len(i))
print('sorted array by insertion sort:')
print(i)


# measuring the run time of each sort
randnums = np.random.randint(1, 500, 500)
insertion = randnums
start = time.time()
InsertionSort.insertionsort(insertion, len(insertion))  # O(n^2)
end = time.time()
print('\nRunning time for Insertion Sort is:', (end - start), 'ms')

selection = randnums
start = time.time()
SelectionSort.selection_sort(selection, len(selection))  # O(n^2)
end = time.time()
print('Running time for Selection Sort is:', (end - start), 'ms')


heap = randnums
start = time.time()
HeapSort.heapSort(heap)  # O(nlogn)
end = time.time()
print('Running time for Heap Sort is:', (end - start), 'ms')

merge = randnums
start = time.time()
MergeSort.mergesort(merge, 0, len(merge) - 1)  # O(nlogn)
end = time.time()
print('Running time for Merge Sort is:', (end - start), 'ms')

quick = randnums
start = time.time()
QuickSort.QuickSort(quick, 0, len(quick))  # Worest Case O(n^2) & Best and Av O(nlogn)
end = time.time()
print('Running time for Quick Sort is:', (end - start), 'ms')
