# UBC CPEN 333 2021W2  - System Software Engineering

**Calendar description**: Use of operating systems abstractions; real-time systems; principles of concurrent and multi-threaded programming; information structures; introduction to object oriented analysis; design, and modelling using UML; software testing.

## Lab 1
### Part 1: function to calculate the roots of a quadratic equation
Consider the following code template:
```python
# student name:
# student number: 
import math

def solveQuadratic(a: float, b: float, c: float) -> str:
    """
        This function takes the coefficients of a 
        quadratic equation as its three parameters.
        It returns a string that states its roots as
        described in the specification.
    """
    return ("To implement")
        
if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Do not limit your testing to these test cases.
        Make sure that you fully test your code.
    """
    Tests = [(1, 2, 3), (1, 2, 1), (1, 3, 1), (1.5, -8, -0.2)] 
    expectedOutput = ["No real roots", 
                      "The root is -1.00",  
                      "The roots are -0.38 and -2.62",
                      "The roots are 5.36 and -0.02"]
    for i in range(len(Tests)):
        print(f"Test {i} : a={Tests[i][0]}, b={Tests[i][1]} c={Tests[i][2]}")
        result = solveQuadratic(a=Tests[i][0], b=Tests[i][1], c=Tests[i][2])
        print(result)
        assert(result == expectedOutput[i])
```

Complete the function `solveQuadratic` and submit the `Lab1_part1.py` file. 

The function takes `a, b, c` (the coefficients) and calculates the roots of the quadratic equation. If there is no real roots, it returns the string `"No real roots"`, if there is exactly one root, it returns the string `"The root is r1"` (replace `r1` with the value). If there are two roots, it returns the string `"The roots are r1 and r2` (replace `r1` and `r2` with their values). The numbers are formatted to have a precision of 2 digits after the decimal point (i.e. `.2f`, as in `print(f"{x:.2f}")` ).

### Part 2: function to print a pyramid of numbers 

This is the typical nested loop exercise. Complete the function `displayPyramid` that prints a pyramid of numbers based on size as shown in the provided test cases.

Consider the following code template:

```python
# student name:
# student number: 
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
    pass # remove this line, it is here for now for the code to be valid
        
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
```

Complete the function `displayPyramid` and submit the `Lab1_part2.py` file.

The expected output for the test cases in the code above is:

```
1
  1
2 1 2
    1
  2 1 2
3 2 1 2 3
      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
          1
        2 1 2
      3 2 1 2 3
    4 3 2 1 2 3 4
  5 4 3 2 1 2 3 4 5
6 5 4 3 2 1 2 3 4 5 6
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
              1
            2 1 2
          3 2 1 2 3
        4 3 2 1 2 3 4
      5 4 3 2 1 2 3 4 5
    6 5 4 3 2 1 2 3 4 5 6
  7 6 5 4 3 2 1 2 3 4 5 6 7
8 7 6 5 4 3 2 1 2 3 4 5 6 7 8
                1
              2 1 2
            3 2 1 2 3
          4 3 2 1 2 3 4
        5 4 3 2 1 2 3 4 5
      6 5 4 3 2 1 2 3 4 5 6
    7 6 5 4 3 2 1 2 3 4 5 6 7
  8 7 6 5 4 3 2 1 2 3 4 5 6 7 8
9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9
```

### Part 3: using turtle to draw Olympic Rings 

In this part of the lab, you are to use the methods available in the turtle module to write a python script that draws the Olympic logo (the five interlocking circles, https://olympics.com/ioc/olympic-rings).

You must use looping in your code (that is, do not just write a long list of statements without any loops). One way to do so is to use the python’s list type.

Notes:
- Examine the documentation: https://docs.python.org/3/library/turtle.html (Links to an external site.). Technically the methods you need are: turtle.penup(), turtle.pendown(), turtle.color(), turtle.circle(), turtle.goto(), turtle.hideturtle(), turtle.done().
- For consistency, use a radius of 45.
- The colours must exactly match the official Olympic ring colours. (https://olympics.com/ioc/olympic-rings (Links to an external site.))
- Don’t be concerned about the interlocking pattern of rings. The order in which the rings are drawn does not matter.

Turtle is a built-in python graphics module that is used for educational purposes. It is quite easy and fun to use.


