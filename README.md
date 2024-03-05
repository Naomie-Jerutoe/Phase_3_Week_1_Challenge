# Phase_3_Week_1_Challenge

## Author

Naomi C Lagat

## Challenge 1: Equal Brick Distribution 

### Description

This challenge aims to determine the minimum number of moves required to distribute a set of bricks equally among a given number of boxes. The function takes an array A representing the number of bricks in each box and returns the minimum moves needed or -1 if equal distribution is not possible.

### Approach

The function iterates through the array, adjusting the number of bricks in each box to achieve equal distribution. It returns the minimum moves if successful; otherwise, it returns -1.

### Usage

result = solution([7, 15, 10, 8])
print(result)  # Output => 7

result2 = solution([11, 10, 8, 12, 8, 10, 11])
print(result2)  # Output => 6

result3 = solution([7, 14, 10])
print(result3)  # Output => -1

## Challenge 2: Maximum Digit Sum Pair

### Description

This challenge involves finding the maximum sum of two numbers in an array that share the same digit sum. The function digit_sum calculates the sum of digits, and the solution function iterates through the array to find and return the maximum sum or -1 if no matching digit sums are found.

### Approach

The function uses a list to store the sum of digits and the corresponding number, iterates through the array, and updates the maximum sum if a pair with the same digit sum is found.

### Usage

result = solution([51, 71, 17, 42])
print(result)  # Output => 93

result2 = solution([42, 33, 60])
print(result2)  # Output => 102

result3 = solution([51, 32, 43])
print(result3)  # Output => -1

## Challenge 3: Alphabetical String

### Description

This challenge aims to generate a string with equal occurrences of each letter from the alphabet based on a given number N. The function solution takes N as input and returns the resulting string.

### Approach

The function calculates the number of letters needed for each letter to occur equally, determines the remaining letters, and constructs the result string accordingly.

### Usage

N1 = 3
print(solution(N1))  # Output "abc"

N2 = 5
print(solution(N2))  # Output "abcde"

N3 = 30
print(solution(N3))  # Output is "abcdefghijklmnoabcdefghijklmno"

## License

MIT License
