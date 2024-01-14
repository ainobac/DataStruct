def pairs(s):
    sum = 0
    posit = []

    for i in range(len(s)):
        if s[i] == '1':
            posit.append(i)
  
    for i in range(len(posit)):
        sum += i*posit[i]-(len(posit)-i-1)*posit[i]
    
    return sum

