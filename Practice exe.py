# Print Numbers
# Write a program to print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)
# Even Numbers
# Print all even numbers between 1 and 20.
for j in range(1,21):
    if j%2==0:
        print(j)

# Sum of Numbers
# Write a program to find the sum of all numbers from 1 to 50.
total_sum=0
for k in range(1,51):
    total_sum+=k
print("Total sum of 1 to 51 is :",total_sum)


# Reverse Counting
# Print numbers from 10 to 1 in reverse order.
for l in range(10,0,-1):
    print(l)


# Multiplication Table
# Display the multiplication table for a number provided by the user.
start=int(input("Enter the start number of the multiplication table:"))
end=int(input("Enter the end number of the multiplication table:"))

for num in range(start,end+1):
    print(f"\nMultiplication table of {num}")
    for i in range (1,11):
        print(f"{num} x {i}={num * i}")


# Factorial Calculation
# Find the factorial of a given number (e.g., 5! = 5 × 4 × 3 × 2 × 1).
import math
nums=int (input("Enter number to get factorial:"))

def factorial(nums):
    return math.factorial(nums)
print(f"Factorial of {nums} is :",factorial(nums))



