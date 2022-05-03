from sqlalchemy import Integer


class Solution:
   def countPrimeString(number):
      primes = set()
      count = 0
      for i in range(len(number)):
         if helper(number[0:i], primes):
            count += 1

   def helper(self, number, primes) -> bool:
      for i in range(1, 7):
         s = number[-i]
         if self.isprime(s):
            ret = self.helper(number[:i], primes)
            if ret == True:
               continue

         else:
            continue



   def isprime(self, numStr, primes):
      num = int(numStr)
      if num in primes:
         return True

      if num <= 1:
         return False

      i = 2
      while i*i <= num:
         if num%i == 0:
            return False
         i += 1
      primes.add(num)
      return True