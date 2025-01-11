# 1. Create a function that adds several numbers
def add_nums(*args):
    total = sum(args)  # Calculate the sum of all provided numbers
    return total

print("Sum of numbers (1, 2, 3, 4, 5):", add_nums(1, 2, 3, 4, 5))   
print("Sum of numbers (1, 20, 30, 40)):", add_nums(1, 20, 30, 40))

#Without the * you have to pass it as a list eg print(add_numbers([1, 2, 3]))





# 2. Create a function that calculates the factorial of a number
import math

def factorial(n):
   
    return math.factorial(n)  
print("Factorial of 7:", factorial(7))





#Mathematical Functions examples
#  Calculate the power of a number
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}")

# Calculate the absolute value of a number
negative_number = -15
absolute_value = math.fabs(negative_number)
print(f"The absolute value of {negative_number} is {absolute_value}")





#4.Examples of functions and how they are implemented 

#function checks if a number is even or odd.
def is_even_or_odd(number):

    return "Even" if number % 2 == 0 else "Odd"
print("Number 7 is:", is_even_or_odd(7))

#This function returns the largest number in a list.
def find_largest(numbers):
  
    return max(numbers, default="List is empty")

print("Largest number in the list [10, 20, 30, 40]:", find_largest([10, 20, 30, 40]))
print("Largest number in the list []:", find_largest([]))