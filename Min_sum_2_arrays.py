def min_possible_sum(N, A, B):
    A.sort()
    B.sort(reverse=True)
    
    min_sum = 0
    for i in range(N):
        min_sum += A[i] * B[i]
    
    return min_sum
N = int(input())
A = list(map(int, input().split()))  
B = list(map(int, input().split()))

print(min_possible_sum(N, A, B))