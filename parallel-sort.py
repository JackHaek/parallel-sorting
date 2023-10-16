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

if __name__ == '__main__':
    processes = multiprocessing.cpu_count()
    print('Processes: ', processes)
    p = Pool(processes=processes)
    print(p.map(f, [1, 2, 3, 4, 5]))

    myArray = [1,0,2,9,3,8,4,7,5,6]
    quick_sort_single_thread(myArray, 0, len(myArray)-1)
    print(myArray)