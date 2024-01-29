def insertionsort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i
        while j > 0 and a[j - 1] > key:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = key