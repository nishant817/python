"""Returns all the prime factors of a positive integer"""
def prime_factors(n):    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(136)
print(pfs)
largest_prime_factor = max(pfs) # The largest element in the prime factor list
print(largest_prime_factor)

###############################################

# Check if a number is prime
def isPrimt(num):
   if num <= 1:
      return False

   i = 2
   while i*i <= num:
      if num%i == 0:
         return False
      i += 1
   return True
