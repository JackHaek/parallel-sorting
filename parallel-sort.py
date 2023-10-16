import numpy as np
import multiprocessing
from multiprocessing import Pool

def f(x):
    return x*x

def quick_sort_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i + 1

def quick_sort_single_thread(arr, low, high):
    if low < high:
        pi = quick_sort_partition(arr, low, high)

        quick_sort_single_thread(arr, low, pi - 1)

        quick_sort_single_thread(arr, pi + 1, high)

def merge_sort_single_thread(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_single_thread(left)
        merge_sort_single_thread(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1 
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2

        merge_sort(low, mid)
        merge_sort(mid + 1, high)

        merge(arr, low, mid, high)

def merge_sort_threaded(arr):
    merge_sort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    processes = multiprocessing.cpu_count()
    print('Processes: ', processes)
    p = Pool(processes=processes)
    print(p.map(f, [1, 2, 3, 4, 5]))

    toCopy = [1,0,2,9,3,8,4,7,5,6]
    myArray = toCopy.copy()
    quick_sort_single_thread(myArray, 0, len(myArray)-1)
    print(myArray)

    myArray = toCopy.copy()
    merge_sort_single_thread(myArray)
    print(myArray)

    myArray = toCopy.copy()
    p.map(merge_sort_threaded, myArray)
    print(myArray)