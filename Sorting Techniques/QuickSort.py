import random


def partition(ArrayOfUnsorted, IndexOfLeft, IndexOfRight):
    pivot = ArrayOfUnsorted[IndexOfLeft]
    index = IndexOfLeft + 1
    for j in range(IndexOfLeft + 1, IndexOfRight):
        if ArrayOfUnsorted[j] < pivot:
            ArrayOfUnsorted[j], ArrayOfUnsorted[index] = ArrayOfUnsorted[index], ArrayOfUnsorted[j]
            index += 1
    ArrayOfUnsorted[IndexOfLeft], ArrayOfUnsorted[index - 1] = ArrayOfUnsorted[index - 1], ArrayOfUnsorted[IndexOfLeft]
    return index - 1


def QuickSort(ArrayOfUnsorted, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        ArrayOfUnsorted[pivot], ArrayOfUnsorted[left] = ArrayOfUnsorted[left], ArrayOfUnsorted[pivot]
        #            x,y = y,x
        pivot_index = partition(ArrayOfUnsorted, left, right)
        QuickSort(ArrayOfUnsorted, left, pivot_index)
        QuickSort(ArrayOfUnsorted, pivot_index + 1, right)