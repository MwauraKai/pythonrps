#checking leap year
def is_leap_year(year):
#divisible by 4 and not divisible by 100 unless divisile by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year 
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



#Find the largest of three numbers.
def find_largest(a, b, c):
    
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find and display the largest number
largest = find_largest(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")






# 1. Number Guessing Game with a while loop

import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))  # Take input from the user
    
    if guess == target_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break  # Exit the loop when the guess is correct
    elif guess < target_number:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")



# 2. Print a Right-Angle Triangle Using Stars with Nested Loops
rows = int(input("Enter the number of rows for the triangle: "))

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop to print stars in each row
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line after each row


# 3. Iterate Over a String Using a for Loop
    # Input string
text = input("Enter a string: ")

print("Iterating over the string:")
for letter in text:
    print(letter)  # Print each letter on a new line

# 4. Print Multiplication Tables

# Input range of numbers for multiplication tables
start = int(input("Enter the starting number for multiplication tables: "))
end = int(input("Enter the ending number for multiplication tables: "))

for num in range(start, end + 1):
    print(f"\nMultiplication Table for {num}")
    for i in range(1, 11):  # Multipliers from 1 to 10
        print(f"{num} x {i} = {num * i}")

