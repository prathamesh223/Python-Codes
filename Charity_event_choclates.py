def total_chocolates(n):
    base_sum = (n * (n + 1)) // 2
    additional_chocolates = 0
    
    for i in range(5, n + 1, 5):
        if i - 1 >= 1:
            additional_chocolates += 2
        if i + 1 <= n:
            additional_chocolates += 2
        elif i == n:
            additional_chocolates += 2  # Circular: Add extra chocolates to child 1 when i == n
    
    return additional_chocolates + base_sum
n=int(input())
print(total_chocolates(n))