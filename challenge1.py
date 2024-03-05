def solution(A):
    N = len(A)
    
    # Calculate the total number of bricks in the array
    total_bricks = sum(A)
    
    # Check if it's possible to distribute the bricks equally
    if total_bricks % N != 0:
        return -1
    
    # Calculate the target number of bricks in each box
    target_per_box = total_bricks // N
    
    # Calculate the minimum moves needed to reach the target in each box
    moves = 0
    for i in range(N - 1):
        diff = A[i] - target_per_box
        A[i + 1] += diff
        moves += abs(diff)
    
    # Check if the final distribution is valid
    if A[-1] == target_per_box:
        return moves
    else:
        return -1

#test cases
result = solution([7, 15, 10, 8])
print(result)  # Output => 7

result2 = solution([11, 10, 8, 12, 8, 10, 11])
print(result2)  # Output => 6

result3 = solution([7, 14, 10])
print(result3)  # Output => -1