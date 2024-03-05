def digit_sum(n):
    # Function to calculate the sum of digits of a number
    return sum(int(digit) for digit in str(n))

def solution(A):
    # Initialize the maximum sum to -1
    max_sum = -1
    # Dictionary to store the sum of digits and the corresponding number
    digit_sums = {}

    # Iterate through each number in the array
    for num in A:
        # Calculate the sum of digits for the current number
        current_sum = digit_sum(num)

        # Check if a number with the same sum of digits has been seen before
        if current_sum in digit_sums:
            # Calculate the sum of the current pair of numbers
            pair_sum = digit_sums[current_sum] + num
            # Update the maximum sum if the current pair has a higher sum
            max_sum = max(max_sum, pair_sum)
        else:
            # If no number with the same sum of digits has been seen, store the current number
            digit_sums[current_sum] = num

    # Return the maximum sum of two numbers with equal digit sums
    return max_sum

#test cases
result = solution([51, 71, 17, 42])
print(result)  # Output => 93

result2 = solution([42, 33, 60])
print(result2)  # Output => 102

result3 = solution([51, 32, 43])
print(result3)  # Output => -1

