import time
import numpy as np


def selection_sort(a, n):
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if a[j] < a[mini]:
                mini = j
        (a[i], a[mini]) = (a[mini], a[i])