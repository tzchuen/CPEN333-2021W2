# Lab4

The objective of this lab is to practice writing multithreading programs using python.

## Multithreaded sorting program

In this lab we will implement a multithreaded sorting program that sorts a list of integers (assume with a length always divisible by two). 

As threads within a process shared the data section, we are going to use four shared variables in our program: `testcase`, `sortedFirstHalf`, `sortedSecondHalf`, and `SortedFullList`.

The program uses three threads to complete the sorting task: two sorting threads and one merging thread. The two sorting threads use the method `sortingWorker` function. The merging thread uses the method `mergingWorker`.

Depending on the function argument `firstHalf`, the sorting threads sort either the first half of the list or the second half of the list, and to store the result in either `sortedFirstHalf`, or `sortedSecondHalf` respectively.

The sorting is ascending, so `[12, -1, 7, 7, 3, 50, 6, 8]` after sorting will be `[-1, 3, 6, 7, 7, 8, 12, 50]`. You can implement any sorting algorithm of your choice but you **are to code the algorithm**. That is, using the `sort()` method for lists, or `sorted()`, or the like is not allowed. 

Consider the following code template:

```python
#student name:
#student number:

import threading

def sortingWorker(firstHalf: bool) -> None:
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
    pass #to Implement

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    pass #to Implement

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 


    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)

```

Implement the two functions first, and then complete the code under the  `if __name__ == "__main__"`: section. 

Notes and Hints:
* Use `import threading`, `threading.Thread()`, `start()` and `join()`.
* The shared variables are great help in allowing threads to work on the data and share the result. Note that no two threads should work on the same shared data, so synchronization is not an issue (so no need for locks ...)
* We are not using any thread pools.
* We are using procedural paradigm for the code in this lab (to focus on threading) but it is easy to rewrite the code using OOP if we wanted to. 
* All threads are non-daemonic. 


Note: we are ignoring the fact that, as they are defined now, the threads are CPU-bound. I have kept it as such for simplicity and focus on threading. However, if, for example, the list was being provided by a networked database (like via the Internet), then it would be IO.
