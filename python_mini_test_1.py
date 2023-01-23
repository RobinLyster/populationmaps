
"""
MATH26021 - Mini test 1
Student name: Robin Lyster
Student id:   10459970
Student mail: robin.lyster@student.manchester.ac.uk
"""
import math
# Feel free to other functions you find useful.
def prime(n):
    """
    Returns `True` if `n` is a prime number and `False` otherwise.
    This was problem 3 of the week 3 home exercises.
    """
    if n < 2:
        return False
    for k in range(2, math.ceil(math.sqrt(n))+1):
#More efficient to only go up to square root
        if n % k == 0:
            return False
    return True
def fibonacci(n):
    """
    Checks if n is fibonacci number, boolean output.

    """
    fibonacci_one = 0
    fibonacci_two = 1
    fibonacci_check = 0
    maximum_possible = 11
    if n > 90:
        maximum_possible = math.floor(math.log(n, 1.5))
#The variable maximum_possible is set to the highest possible fibonacci
#number n could be, since (for the 11th and subsequent fibonacci number
#Fib(x), Fib(x)>1.5**x). This makes this section code of complexity O(log(n),
#which is less complex than the prime number checker, which is O(sqrt(n)).)
    for i in range(maximum_possible):
        fibonacci_check = fibonacci_one + fibonacci_two
        if i%2 == 0:
            fibonacci_one = fibonacci_check
        else:
            fibonacci_two = fibonacci_check
        if n == fibonacci_check:
            return True
def isbn_final_digit(n):
    """
    Uses the first 12 digits of an integer to calculate the final digit
    of an isbn, output is an integer.
    """
    final_digit = 0
    for i in range(0, 11, 2):
        final_digit = final_digit + int(str(n)[i])
    for i in range(1, 12, 2):
        final_digit = final_digit + 3 * int(str(n)[i])
    final_digit = (10-final_digit)%10
    return final_digit
# Problem 1
def fiboprime(n):
    """
    Returns `True` if `n` is a fibonacci prime number and `False` otherwise.
    """
    if prime(n) == True:
        if fibonacci(n) == True:
            return True
    return False

# Problem 2
def sexyprime(n):
    """
    Returns `True` if `n` is a sexy prime number and `False` otherwise.
    """
    for i in range(n):
        if prime(n-i) == True:
            if prime(n-i+6) == True:
                return n-i
    return

# Problem 3
def isbn(n, mode):
    """
    Either calculates the final isbn digit from the other 12, or checks if
    a given final digit matches the preceding 12. Either integer or boolean
    output, for calculate and verify, respectively.
    """
    if mode == 'calculate':
        if abs(n) != n:
            return
        if len(str(n)) != 12:
            return
        return int(isbn_final_digit(n))
    else:
        if isbn_final_digit(n) == int(str(n)[12]):
            return True
        return False
# main() function for all the testing
def main():
    """
    Performs functions to check if they're working properly, outputs strings.'
    """
    print("should return True:   ", fiboprime(1597))
    print("should return False:  ", fiboprime(-7))
    print("should return 23:     ", sexyprime(25))
    print("should return True:   ", isbn(9781461471370, ))

main() # call main() function to run all tests
