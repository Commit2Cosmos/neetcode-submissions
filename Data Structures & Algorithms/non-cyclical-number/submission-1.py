class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:

            summ = 0

            for digit_str in str(n):
                summ += int(digit_str)**2
            
            if summ == 1:
                return True
            
            if summ in seen:
                return False
            
            seen.add(summ)

            n = summ