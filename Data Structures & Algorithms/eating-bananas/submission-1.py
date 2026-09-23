class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left<right:
            rate = (left+right)//2
            total_h = 0
            
            for pile in piles:
                total_h += (pile + rate - 1) // rate

            if total_h > h:
                left = rate+1
            else:
                right = rate
            
        return left