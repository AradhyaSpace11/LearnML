# Read the number of problems
n = int(input())

# Initialize a counter for the number of problems they will implement
problems_to_solve = 0

# Loop over the number of problems
for _ in range(n):
    # Read the three values for each problem
    petya, vasya, tonya = map(int, input().split())
    
    # Check if at least two friends are sure (i.e., sum of the three is 2 or more)
    if petya + vasya + tonya >= 2:
        problems_to_solve += 1

# Output the result
print(problems_to_solve)
