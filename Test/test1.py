def isPrime(n, i = 2):
 
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True 
    return isPrime(n, i + 1)

def primeCount(_n):
    counter = 0
    for i in range(2, _n):
        if isPrime(i):
            counter += 1
    return counter

    
print(primeCount(500))