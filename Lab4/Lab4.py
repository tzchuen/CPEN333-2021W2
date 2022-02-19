#student name: Zhi Chuen Tan
#student number: 65408361

from heapq import merge
import threading

# implements quick sort, adapted from the pseudocode obtained from https://www.geeksforgeeks.org/quick-sort/
def quickSort(arr: list, start: int, end: int):
    if start < end:
        pivotIndex = partition(arr, start, end)

        quickSort(arr, start, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, end)
    

# partition function for the quick sort algorithm, adapted from pseudocode at https://www.geeksforgeeks.org/quick-sort/
def partition(arr: list, start: int, end:int):
    
    pivotElement = arr[end]

    i = start - 1

    for j in range(start, end):
        if arr[j] < pivotElement: 
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i + 1], arr[end] = arr[end], arr[i + 1] 
    return (i + 1)

def sortingWorker(firstHalf: bool):
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    global sortedFirstHalf
    global sortedSecondHalf

    if firstHalf:
        quickSort(sortedFirstHalf, 0, len(sortedFirstHalf) - 1)
        
    else:
        quickSort(sortedSecondHalf, 0, len(sortedSecondHalf) - 1)

# implements merge function used in merge sort, adapted from https://www.geeksforgeeks.org/merge-sort/
def mergingWorker():
    """ This function uses the two shared variables 
        sortedSecondHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        shared variable sortedFullList.
    """

    # tells the interpreter that these are global variables
    global sortedFirstHalf
    global sortedSecondHalf
    global SortedFullList

    # concatnates the two halves into a full list
    SortedFullList = sortedFirstHalf + sortedSecondHalf

    i = j = k = 0

    while i < len(sortedFirstHalf) and j < len(sortedSecondHalf):
        if sortedFirstHalf[i] < sortedSecondHalf[j]:
            SortedFullList[k], sortedFirstHalf[i] = sortedFirstHalf[i], SortedFullList[k]
            i += 1
        
        else:
            SortedFullList[k], sortedSecondHalf[j] = sortedSecondHalf[j], SortedFullList[k]
            j += 1
        k += 1

    while i < len(sortedFirstHalf):
        SortedFullList[k], sortedFirstHalf[i] = sortedFirstHalf[i], SortedFullList[k]
        i += 1
        k += 1
  
    while j < len(sortedSecondHalf):
        SortedFullList[k] = sortedSecondHalf[j]
        j += 1
        k += 1


if __name__ == "__main__":
    #shared variables
    testcase = [12, -1, 7, 7, 3, 50, 6, 8]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    # first split the testcase into first and second halves
    sortedFirstHalf = testcase[0 : len(testcase) // 2]
    sortedSecondHalf = testcase[len(testcase) // 2 : len(testcase)]

    # to implement the rest of the code below, as specified
    firstHalfSortThread = threading.Thread(target = sortingWorker, args = (True,))
    secondHalfSortThread = threading.Thread(target = sortingWorker, args = (False,))
    mergeThread = threading.Thread(target = mergingWorker)

    # starts the sorting threads
    firstHalfSortThread.start()
    secondHalfSortThread.start()
    firstHalfSortThread.join()
    secondHalfSortThread.join()

    # starts the merging thread
    mergeThread.start()
    mergeThread.join()
    
    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)