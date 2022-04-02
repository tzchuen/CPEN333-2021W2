from socket import *
import time
import random

# requirements defined in project spec
serverName = "localhost"
serverPort = 12000

SEC_MS = 1000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))

print("Server is ready to receive!")


while True:
    # creates a list of 10 boolean variables, 1 of which is True, while rest are False (i.e. 10% chance of selecting True)
    lossList = [True] + [False] * 9
    packetLoss = random.choice(lossList)    # if True chosen, then the packet will be "lost"

    if packetLoss:
        pass    # do nothing if packet loss occurs
    
    else:
        delayTime = random.randint(5,50) # random RTT between 5-50ms
        print(f"DEBUG: delay = {delayTime}")

        time.sleep(delayTime/SEC_MS)    # convert seconds to milliseconds
        
        message, clientAddress = serverSocket.recvfrom(2048)
        returnMessage = "ditto"
        serverSocket.sendto(returnMessage.encode(), clientAddress)
