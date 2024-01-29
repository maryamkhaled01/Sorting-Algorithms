def mergesort(a, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(a, low, mid)
        mergesort(a, mid + 1, high)
        merge(a, low, mid, high)


def merge(a, low, mid, high):
    nl = mid - low + 1
    nr = high - mid
    l = []
    r = []
    for i in range(nl):
        l.append(a[low + i])
    for j in range(nr):
        r.append(a[mid + 1 + j])
    i = 0
    j = 0
    k = low
    while i < nl and j < nr:
        if l[i] < r[j]:
            a[k] = l[i]
            i = i + 1
            k = k + 1
        else:
            a[k] = r[j]
            j = j + 1
            k = k + 1
    while i < nl:
        a[k] = l[i]
        i = i + 1
        k = k + 1
    while j < nr:
        a[k] = r[j]
        j = j + 1
        k = k + 1
