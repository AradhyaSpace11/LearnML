lis = [0,3,2,1,5,2]
n = 6
ex = 3



def maximum_possible_x(t, test_cases):
    results = []
    
    for case in test_cases:
        n, arr = case
        # Find the two largest numbers
        largest = max(arr)
        arr.remove(largest)
        second_largest = max(arr)
        
        # Calculate the maximum possible value of x
        max_x = (largest + second_largest) // 2
        results.append(max_x)
    
    return results

t = 3
test_cases = [
    (6, 3, [0, 3, 2, 1, 5, 2]),
    (6, 2, [1, 3, 4, 1, 0, 2]),
    (4, 5, [2, 5, 10, 3])
]

output = maximum_mex(t, test_cases)
for result in output:
    print(result)

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Get results
output = maximum_possible_x(t, test_cases)
for result in output:
    print(result)


