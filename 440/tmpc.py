t = int(input())
results = []
for _ in range(t):
    n, w = map(int, input().split())
    c = list(map(int, input().split()))
    
    cost = [0] * (2 * w)
    for i in range(n):
        cost[i % (2 * w)] += c[i]
    
    current_sum = sum(cost[:w])
    min_cost = current_sum
    
    for i in range(1, 2 * w):
        current_sum = current_sum - cost[i - 1] + cost[(i + w - 1) % (2 * w)]
        min_cost = min(min_cost, current_sum)
    
    results.append(min_cost)

print('\n'.join(map(str, results)))