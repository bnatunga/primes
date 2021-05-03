#faster check for primes
import math

def is_prime_fast(n):
    if n<2 or n>2 and n%2 == 0:
        return False
    for b in range(2, (math.floor((math.sqrt(n)))+1)):
        if n%b == 0:
            return False
    return True

print(is_prime_fast(29))

def get_primes_fast(n):
    primes_fast=[]
    for x in range(n+1):
        if is_prime_fast(x):
            primes_fast.append(x)
    return primes_fast

print(get_primes_fast(17))