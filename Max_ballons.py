def max_balloons(n, budget, balloons, costs):
    if n < 2:
        return 0  # Not enough packets to choose 2
    
    packets = [(balloons[i], costs[i]) for i in range(n)]
    packets.sort(key=lambda x: x[1])
    
    left, right = 0, n - 1
    max_balloons = 0
    
    while left < right:
        total_cost = packets[left][1] + packets[right][1]
        
        if total_cost <= budget:
            total_balloons = packets[left][0] + packets[right][0]
            max_balloons = max(max_balloons, total_balloons)
            left += 1
        else:
            right -= 1
    
    return max_balloons
n=int(input())
budget=int(input())
balloons=[int(x) for x in input().split()]
costs=[int(x) for x in input().split()]
print(max_balloons(n, budget, balloons, costs))