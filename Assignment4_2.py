# Ask the user for input N
N = int(input("Enter a positive integer N: "))

# Initialize a list to store the N numbers
numbers = []

# Ask the user for N numbers
for i in range(N):
    num = int(input(f"Enter number {i+1} of {N}: "))
    numbers.append(num)

# Ask the user for input X
X = int(input("Enter an integer X: "))

# Check if X is in the list of numbers
if X in numbers:
    index = numbers.index(X) + 1
else:
    index = -1

# Output the result
print(index)