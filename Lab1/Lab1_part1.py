# student name: Zhi Chuen Tan
# student number: 65408361

import math
from uuid import RFC_4122

def solveQuadratic(a: float, b: float, c: float) -> str:
    """
        This function takes the coefficients of a 
        quadratic equation as its three parameters.
        It returns a string that states its roots as
        described in the specification.
    """

    # discriminant
    disc: float = (b**2) - (4*a*c)

    if disc < 0:
        return ("No real roots")

    elif disc == 0:
        r1: float = (-1*b) / (2*a)  
        return (f"The root is {r1:.2f}")
    
    else:
        r1: float = (-1*b + math.sqrt(disc)) / (2*a)
        r2: float = (-1*b - math.sqrt(disc)) / (2*a)

        # # displays smaller root 1st
        # if r1 < r2:
        return (f"The roots are {r1:.2f} and {r2:.2f}")
        
        # else:
        #     return (f"The roots are {r2:.2f} and {r1:.2f}")
        
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