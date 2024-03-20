
def count_vowels(word):
    """ Question 01: Function to count the number of vowels in a word."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


""" Question 02: Iterate through all the animals."""
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

""" Question 03: Iterate through 1-20."""
# Iterate from 1 to 20
for i in range(1, 21):
    # Check if number is odd or even
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

""" Question 04: Function to calculate the sum of two integers.."""
def sum_of_integers(a, b):
    return a + b

# Get input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Call the function and print the result
result = sum_of_integers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)
