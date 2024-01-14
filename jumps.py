def jumps(n, a, b):
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(1,n+1):
        if i-a >= 0:
            ways[i] += ways[i-a]
        if i-b >= 0:
            ways[i] += ways[i-b]
    return ways[n]
