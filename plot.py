import numpy as np
import matplotlib.pyplot as plt
from merge import mergeSort
from insertion import insertion
import time

def random(n: int):
    return [np.random.randint(0, 1000000) for _ in range(n)]

def compare(n: int):
    randomArray = random(n)
    
    start = time.time()
    mergeSort(randomArray)
    stop = time.time()
    mergeTime = stop - start
    
    start = time.time()
    insertion(randomArray)
    stop = time.time()
    insertionTime = stop - start

    return insertionTime, mergeTime

def main():
    sizes = [1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000]
    insertionTimes = []
    mergeTimes = []

    for size in sizes:
        insertionTime, mergeTime = compare(size)
        insertionTimes.append(insertionTime)
        mergeTimes.append(mergeTime)

    plt.plot(sizes, insertionTimes, label='Insertion Sort')
    plt.plot(sizes, mergeTimes, label='Merge Sort')

    plt.xlabel('Size of an Array')
    plt.ylabel('Time')
    plt.title('INSERTION SORT VS MERGE SORT')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()