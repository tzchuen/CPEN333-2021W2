#student name: Zhi Chuen Tan
#student number: 65408361

import multiprocessing
import random #is used to cause some randomness 
import time
from turtle import left   #is used to cause some delay to simulate thinking or eating times

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

       
        # first take the left chopstick
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")

        # we want non-blocking acquire, so the process is not blocked when we try to acquire a taken semaphore
        rightChopstickAvailable = chopstick[rightChopstick].acquire(False)

        # if the right chopstick is unavailable, release the left chopstick and wait
        if not rightChopstickAvailable:
            print(f"DEBUG: philosopher{id} is to release the left chopstick {leftChopstick}, as the right chopstick {rightChopstick} is unavailable")
            chopstick[leftChopstick].release()

        # if the right chopstick is available, the philosopher can eat
        else:
            print(f"DEBUG: philosopher{id} has chopstick {rightChopstick}")
            eatForAWhile()  #use this line as is
            print(f"DEBUG: philosopher{id} is to release chopstick {rightChopstick}")
            chopstick[rightChopstick].release()
            print(f"DEBUG: philosopher{id} is to release chopstick {leftChopstick}")
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