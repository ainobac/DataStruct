def split(A):
    small = [A[0]]
    high = A[1:]
    ways = 0

    for i in range(1,len(A)):
        if min(high) > max(small):
            small.append(high[0])
            del high[0]
            ways += 1

        else:
            small.append(A[i])
            del high[0]
            
    return ways


