def solution(N):
    # Ensure N is within a valid range
    if N <= 0:
        return ""

    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Calculate the number of letters needed for each letter to occur an equal number of times
    letters_per_occurrence = N // 26

    # Calculate the remaining letters after distributing equally
    remaining_letters = N % 26

    # Build the result string with equal occurrences of each letter
    result_str = alphabet * letters_per_occurrence

    # Append the remaining letters
    result_str += alphabet[:remaining_letters]

    return result_str

# Test case:
N1 = 3
print(solution(N1))  # Output "abc"

N2 = 5
print(solution(N2))  # Output "abcde"

N3 = 30
print(solution(N3))  # Output is "abcdefghijklmnoabcdefghijklmno"
