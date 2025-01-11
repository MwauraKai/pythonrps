# Simple Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
#This prompts the user for two numbers
num_1= int(input("Enter first number:"))
num_2=float(input("Enter second number:"))

sum=num_1+num_2
diff=num_1-num_2
multiplication=num_1*num_2
div=num_1/num_2

print("sum is:",sum,"\n diff is:",diff,"\n multiplication is:",multiplication,"\n div is:",div)

#2.Generating a random number between 1 and 10using the random library
import random

random_no=random.randint(1,100)
print("random no is:",random_no)

# 3.Program to calculate and print the square root of a given number
import math
number=float(input("Enter number to get square root:"))
sqrt_value=math.sqrt(number)
print("Square root of number is:",sqrt_value)

