import math

def isprime(n):
    if n>1:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
            else:
                return True
    else:
        return False
    