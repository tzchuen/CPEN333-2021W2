# Lab 5: Dinning-philosophers problem 

In this lab, a multiprocessing implementation of the dining-philosophers synchronization problem is provided to you. It is rather based on the code we discussed during the lecture, and as we explained, it is susceptible to deadlock (susceptible is a key word here, you may run the program many many times and deadlock may not happen).

Note that in the provided code, we are using some random delay to simulate the time a philosopher takes to eat or to think.

Consider the following code:

```python
#student name:
#student number:

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        def eatForAWhile():   #simulates philosopher eating time with a random delay
            print(f"DEBUG: philosopher{id} eating")
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        def thinkForAWhile(): #simulates philosopher thinking time with a random delay
            print(f"DEBUG: philosopher{id} thinking")
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers

        #to simplify, try statement not used here
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        chopstick[rightChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")

        eatForAWhile()  #use this line as is

        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()
```

## Part 1

We discussed that one possible solution to avoid deadlock is to "allow a philosopher to pick up her chopsticks only if both chopsticks are available".

You are to modify the code to implement the solution based on the above statement. Submit this part of the lab as `Lab6_part1.py`.

You are allowed to add any additional synchronization primitives that you may need. But don't use more than what is necessary. If used, they must be defined in the main process and be passed to the child processes as one of the args elements for their use (e.g. similar to the chopstick semaphoreList). 


## Part 2: 

We discussed that another possible solution to avoid deadlock is to "use an asymmetric solution, e.g. an odd philosopher picks up first her left chopstick and then her right chopstick, whereas an even philosopher picks up her right first and then her left chopstick".

You are to modify the code to implement the solution based on the above statement. Submit this part of the lab as `Lab6_part2.py`.


A sample output of the original program is:

```
DEBUG: philosopher2 has chopstick2
DEBUG: philosopher2 has chopstick3
DEBUG: philosopher2 eating
DEBUG: philosopher1 has chopstick1
DEBUG: philosopher0 has chopstick0
DEBUG: philosopher4 has chopstick4
DEBUG: philosopher2 is to release chopstick3
DEBUG: philosopher3 has chopstick3
DEBUG: philosopher2 is to release chopstick2
DEBUG: philosopher1 has chopstick2
DEBUG: philosopher1 eating
DEBUG: philosopher2 thinking
DEBUG: philosopher1 is to release chopstick2
DEBUG: philosopher1 is to release chopstick1
DEBUG: philosopher0 has chopstick1
DEBUG: philosopher1 thinking
DEBUG: philosopher0 eating
DEBUG: philosopher2 has chopstick2
DEBUG: philosopher0 is to release chopstick1
DEBUG: philosopher0 is to release chopstick0
DEBUG: philosopher4 has chopstick0
DEBUG: philosopher0 thinking
DEBUG: philosopher4 eating
DEBUG: philosopher1 has chopstick1
DEBUG: philosopher4 is to release chopstick0
DEBUG: philosopher0 has chopstick0
DEBUG: philosopher4 is to release chopstick4
DEBUG: philosopher3 has chopstick4
DEBUG: philosopher4 thinking
DEBUG: philosopher3 eating
DEBUG: philosopher3 is to release chopstick4
DEBUG: philosopher4 has chopstick4
DEBUG: philosopher3 is to release chopstick3
DEBUG: philosopher2 has chopstick3
DEBUG: philosopher3 thinking
DEBUG: philosopher2 eating
DEBUG: philosopher2 is to release chopstick3
DEBUG: philosopher2 is to release chopstick2
DEBUG: philosopher1 has chopstick2
DEBUG: philosopher2 thinking
DEBUG: philosopher1 eating
DEBUG: philosopher3 has chopstick3
DEBUG: philosopher1 is to release chopstick2
DEBUG: philosopher1 is to release chopstick1
DEBUG: philosopher0 has chopstick1
DEBUG: philosopher0 eating
DEBUG: philosopher1 thinking
DEBUG: philosopher2 has chopstick2
DEBUG: philosopher0 is to release chopstick1
DEBUG: philosopher1 has chopstick1
DEBUG: philosopher0 is to release chopstick0
DEBUG: philosopher4 has chopstick0
DEBUG: philosopher0 thinking
DEBUG: philosopher4 eating
DEBUG: philosopher4 is to release chopstick0
DEBUG: philosopher0 has chopstick0
DEBUG: philosopher4 is to release chopstick4
DEBUG: philosopher4 thinking
DEBUG: philosopher3 has chopstick4
DEBUG: philosopher3 eating
DEBUG: philosopher3 is to release chopstick4
DEBUG: philosopher3 is to release chopstick3
DEBUG: philosopher2 has chopstick3
DEBUG: philosopher3 thinking
DEBUG: philosopher2 eating
DEBUG: philosopher4 has chopstick4
DEBUG: philosopher2 is to release chopstick3
DEBUG: philosopher2 is to release chopstick2
DEBUG: philosopher1 has chopstick2
DEBUG: philosopher2 thinking
DEBUG: philosopher1 eating
DEBUG: philosopher3 has chopstick3
DEBUG: philosopher1 is to release chopstick2
DEBUG: philosopher2 has chopstick2
DEBUG: philosopher1 is to release chopstick1
DEBUG: philosopher0 has chopstick1
DEBUG: philosopher0 eating
DEBUG: philosopher1 thinking
DEBUG: philosopher0 is to release chopstick1
DEBUG: philosopher1 has chopstick1
DEBUG: philosopher0 is to release chopstick0
DEBUG: philosopher4 has chopstick0
DEBUG: philosopher0 thinking
DEBUG: philosopher4 eating
DEBUG: philosopher4 is to release chopstick0
DEBUG: philosopher4 is to release chopstick4
DEBUG: philosopher4 thinking
DEBUG: philosopher3 has chopstick4
DEBUG: philosopher3 eating
DEBUG: philosopher0 has chopstick0
DEBUG: philosopher3 is to release chopstick4
DEBUG: philosopher4 has chopstick4
DEBUG: philosopher3 is to release chopstick3
DEBUG: philosopher2 has chopstick3
DEBUG: philosopher3 thinking
DEBUG: philosopher2 eating
DEBUG: philosopher2 is to release chopstick3
DEBUG: philosopher3 has chopstick3
DEBUG: philosopher2 is to release chopstick2
DEBUG: philosopher1 has chopstick2
DEBUG: philosopher2 thinking
DEBUG: philosopher1 eating
DEBUG: philosopher1 is to release chopstick2
DEBUG: philosopher2 has chopstick2
DEBUG: philosopher1 is to release chopstick1
DEBUG: philosopher0 has chopstick1
DEBUG: philosopher0 eating
DEBUG: philosopher1 thinking
DEBUG: philosopher0 is to release chopstick1
DEBUG: philosopher1 has chopstick1
DEBUG: philosopher0 is to release chopstick0
DEBUG: philosopher0 thinking
DEBUG: philosopher4 has chopstick0
DEBUG: philosopher4 eating
DEBUG: philosopher4 is to release chopstick0
DEBUG: philosopher0 has chopstick0
DEBUG: philosopher4 is to release chopstick4
DEBUG: philosopher3 has chopstick4
DEBUG: philosopher3 eating
DEBUG: philosopher4 thinking
DEBUG: philosopher3 is to release chopstick4
DEBUG: philosopher4 has chopstick4
DEBUG: philosopher3 is to release chopstick3
DEBUG: philosopher2 has chopstick3
DEBUG: philosopher3 thinking
DEBUG: philosopher2 eating
DEBUG: philosopher2 is to release chopstick3
DEBUG: philosopher2 is to release chopstick2
DEBUG: philosopher1 has chopstick2
DEBUG: philosopher2 thinking
DEBUG: philosopher1 eating
DEBUG: philosopher3 has chopstick3
DEBUG: philosopher1 is to release chopstick2
DEBUG: philosopher2 has chopstick2
DEBUG: philosopher1 is to release chopstick1
DEBUG: philosopher0 has chopstick1
DEBUG: philosopher0 eating
DEBUG: philosopher1 thinking
DEBUG: philosopher0 is to release chopstick1
DEBUG: philosopher1 has chopstick1
DEBUG: philosopher0 is to release chopstick0
DEBUG: philosopher4 has chopstick0
DEBUG: philosopher0 thinking
DEBUG: philosopher4 eating
DEBUG: philosopher4 is to release chopstick0
DEBUG: philosopher4 is to release chopstick4
DEBUG: philosopher3 has chopstick4
DEBUG: philosopher4 thinking
DEBUG: philosopher3 eating
DEBUG: philosopher0 has chopstick0
DEBUG: philosopher3 is to release chopstick4
DEBUG: philosopher3 is to release chopstick3
DEBUG: philosopher2 has chopstick3
DEBUG: philosopher2 eating
DEBUG: philosopher3 thinking
DEBUG: philosopher4 has chopstick4
DEBUG: philosopher2 is to release chopstick3
DEBUG: philosopher3 has chopstick3
DEBUG: philosopher2 is to release chopstick2
DEBUG: philosopher1 has chopstick2
DEBUG: philosopher1 eating
DEBUG: philosopher2 thinking
DEBUG: philosopher1 is to release chopstick2
DEBUG: philosopher1 is to release chopstick1
DEBUG: philosopher0 has chopstick1
DEBUG: philosopher0 eating
DEBUG: philosopher1 thinking
DEBUG: philosopher0 is to release chopstick1
DEBUG: philosopher0 is to release chopstick0
DEBUG: philosopher4 has chopstick0
DEBUG: philosopher0 thinking
DEBUG: philosopher4 eating
DEBUG: philosopher4 is to release chopstick0
DEBUG: philosopher4 is to release chopstick4
DEBUG: philosopher4 thinking
DEBUG: philosopher3 has chopstick4
DEBUG: philosopher3 eating
DEBUG: philosopher3 is to release chopstick4
DEBUG: philosopher3 is to release chopstick3
DEBUG: philosopher3 thinking
```