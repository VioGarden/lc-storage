class Solution:
    def isHappy(self, n: int) -> bool:
        
        def happy(m):
            count = 0
            for i in m:
                count += int(i)**2
            if count == 1:
                return [True, str(count)]
            return [False, str(count)]
        
        x = [False, str(n)]
        for i in range(30):
            if x[0] == True:
                return True
            x = happy(x[1])
        
        return False