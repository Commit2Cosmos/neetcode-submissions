class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def recur(i, left2total):
            if left2total == 0:
                return 1

            if left2total < 0:
                return 0

            if (i, left2total) in hashmap:
                return hashmap[(i, left2total)]

            hashmap[(i, left2total)] = recur(i, left2total-coins[i]) + (0 if (i == len(coins)-1) else recur(i+1, left2total))

            return hashmap[(i, left2total)]

        hashmap = {}

        return recur(0, amount)