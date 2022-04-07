# Name: Pasit Laothamatas, Zhi Chuen Tan
# Student number: 28570166, 65408361

from socket import *
import time

def client():
    # requirements defined in project spec
    serverName = "localhost"
    serverPort = 12000

    # number of messages sent; start at 1
    messageNumber: int = 1

    # create client UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    print("Welcome!")   # greets user

    message = f"PING {messageNumber} - " + input("Please enter a greeting.\n")  # prompts user for a greeting

    sentTime = time.time()  # start timing when message is sent
    clientSocket.sendto(message.encode(), (serverName, serverPort)) # sends message to server
    returnMessage, serverAddress = clientSocket.recvfrom(2048)  # read reply from socket
    receivedTime = time.time()  # stop timing once message is received

    rttTime = receivedTime - sentTime   # finds the RTT

    if rttTime > 1: # if client receives no response within 1 second, assume packet loss
            print("Request timed out!")

    else:
        print(f"PING {messageNumber} - " + returnMessage.decode())  # prints the received string from server
        print(f"Round Trip Time (RTT) for PING {messageNumber} is: {rttTime}") # prints the RTT

    continueMessage = input("Do you want to continue? y/n \n")  # asks user if they want to send another message to the server

    while continueMessage not in ['y', 'Y', 'n', 'N']:  # ensures valid input
        print("ERROR: Invalid input!")
        continueMessage = input("Do you want to continue? y/n \n")

    while continueMessage in ['y', 'Y']:    # if user wants to send another message, repeat steps to send message to server
        messageNumber += 1  # increase the number of messages sent

        message = f"PING {messageNumber} - " + input("Please enter a greeting.\n")
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        sentTime = time.time()
        returnMessage, serverAddress = clientSocket.recvfrom(2048)
        receivedTime = time.time()

        rttTime = receivedTime - sentTime

        if rttTime > 1:
            print("Request timed out!")
        
        else:
            print(f"PING {messageNumber} - " + returnMessage.decode())
            print(f"Round Trip Time (RTT) for PING {messageNumber} is: {rttTime}")

        continueMessage = input("Do you want to continue? y/n \n")

        while continueMessage not in ['y', 'Y', 'n', 'N']:
            print("ERROR: Invalid input!")
            continueMessage = input("Do you want to continue? y/n \n")

    clientSocket.close()    # user does not want to send any more messages, close client UDP socket
    print("Goodbye!")       # client terminates

if __name__ == "__main__":
    client()    # calls the client function