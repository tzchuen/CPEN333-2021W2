# student name: Zhi Chuen Tan
# student number: 65408361
def displayPyramid(size: int) -> None:
    """
        This method prints a pyramid of size size.
        Implement the method using nested for loops.
        size is an integer between 1 and 9 (inclusive).
        Example: if size is 7, it should print:
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
    """      

    # outer loop controls row number
    for row in range (1, size + 1): 

      # pads left side of the pyramid with spaces
      for num_space in range ( (size - row) * 2, 0, -2): 
        print ("  ", end="") # end="" makes the next print statement print in the same line

      # each row has the same number of elements as the k-th odd number
      for k in range (0, (2 * row) - 1):
    
        # decrements numbers from row number until it reaches 1
        if (row - k) >= 1:
          print (row - k, end=" ")

        # increments numbers from 1 until it reaches row number
        else:
          print (k - row + 2, end=" ")

      # prints new line
      print()


if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Make sure that you fully test your code.
        This prints the output for all rquired 
        sizes, from 1 to 9.
    """
    for size in range (1, 10):
        displayPyramid(size)