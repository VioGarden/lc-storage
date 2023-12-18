class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False
    
    def happy(self, m):
        output = 0
        while m:
            digit = m % 10
            digit = digit ** 2
            output += digit
            m = m // 10
