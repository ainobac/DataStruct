def primes(N):
    if N <= 1 or N >= 10**5:
        return 0
    
    primes = 0
    for i in range (2,N+1):
        prime = True
        for j in range(2, int(i/2)+1):
            if (i % j) == 0:
                prime = False
                break
        if prime:
            primes += 1
    return primes
    