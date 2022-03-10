#student name: Zhi Chuen Tan
#student number: 65408361

import threading
import random #is used to cause some randomness 
import time   #is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implement a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   #initilize a list of length size
                                    #all zeroed (initial value doesn't matter)
        self._in_index = 0   #the in reference point
        self._out_index = 0  #the out reference point

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally.
        """
        self._buffer[self._in_index] = item
        self._in_index = (self._in_index + 1) % SIZE

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally.
        """
        item = self._buffer[self._out_index]
        self._out_index = (self._out_index + 1) % SIZE
        return item

def producer() -> None:
    """
        Implement the producer function to be used by the producer thread.
        It must correctly use full, empty and mutex.
    """

    def waitForItemToBeProduced() -> int: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        return random.randint(1, 99)  #an item is produced

    for _ in range(SIZE * 2): #we just produce twice the buffer size for testing

        item = waitForItemToBeProduced()  #wait for an item to be produced

        if (full._value != SIZE):   # produce if there are less than SIZE items in the buffer
            with mutex:         # uses the mutex lock, entering critical section of producer()
                buffer.insert(item)
                print(f"DEBUG: {item} produced")
                full.release()  # increments the number of full buffers by 1
                empty.acquire() # reduces the number of empty buffers by 1

        else:
            print("DEBUG: Buffer is full! Can't produce any more items.")
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
            

def consumer() -> None:
    """
        Implement the consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex.
    """
    #use the following code as is
    def waitForItemToBeConsumed(item) -> None: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        #to simulate consumption, item is thrown away here by just ignoring it

    for _ in range(SIZE * 2): #we just consume twice the buffer size for testing
        #write the code below to correctly remove an item from the circular buffer

        if empty._value != SIZE: # consumer if there are less than SIZE empty buffers
            with mutex:
                item = buffer.remove() # stores the removed buffer object in item
                waitForItemToBeConsumed(item)  #wait for the item to be consumed
                print(f"DEBUG: {item} consumed")
                full.acquire()  # reduces the number of full buffers by 1
                empty.release() # increases the number of empty buffers by 1

            # mutex.acquire()

            # try:
            #     full.acquire()  # reduces the number of full buffers by 1
            #     empty.release() # increases the number of empty buffers by 1
            #     item = buffer.remove() # stores the removed buffer object in item
            #     waitForItemToBeConsumed(item)  #wait for the item to be consumed
            #     print(f"DEBUG: {item} consumed")
            
            # finally:
            #     mutex.release()

        else:
            print("DEBUG: Buffer is empty! Can't consume any items.")
            time.sleep(round(random.uniform(.1, .3), 2)) # a random delay (100 to 300 ms) 
        

if __name__ == "__main__":
    SIZE = 5  #buffer size
    buffer = circularBuffer(SIZE)  #initialize the buffer

    full = threading.Semaphore(0)         #full semaphore: number of full buffers
                                          #initial value set to 0
    empty = threading.Semaphore(SIZE)     #empty semaphore: number of empty buffers
                                          #initial value set to SIZE
    mutex = threading.Lock()  #lock for protecting data on insertion or removal

    #complete the producer-consumer thread creation below
    producerThread = threading.Thread(target = producer)
    consumerThread = threading.Thread(target = consumer)

    # starts the threads
    producerThread.start()
    consumerThread.start()
    
    producerThread.join()
    consumerThread.join()
    
