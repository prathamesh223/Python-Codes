def sum_divisible_by_x(N, X):
    total_sum = 0
    
    # The last element calculation needs A[N-1] + A[0]
    last_element = N + 1  # A[N] = N and A[1] = 1
    
    # Calculate sums for the first N-1 elements of B
    for i in range(1, N):
        sum_pair = i + (i + 1)
        if sum_pair % X == 0:
            total_sum += sum_pair
    
    # Handle the last element
    if last_element % X == 0:
        total_sum += last_element
    
    return total_sum

# Example usage
input1 = 9       
input2 = 2
print(sum_divisible_by_x(input1, input2))
