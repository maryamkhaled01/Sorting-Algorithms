def heapify(arr, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        max = l
    if r < n and arr[max] < arr[r]:
        max = r
    if max != i:
        (arr[i], arr[max]) = (arr[max], arr[i])
        heapify(arr, n, max)


def heapSort(arr):
    n = len(arr)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
