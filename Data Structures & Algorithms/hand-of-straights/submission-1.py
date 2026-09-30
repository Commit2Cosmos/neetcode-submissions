class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        freqs = {}

        for x in hand:
            if x in freqs:
                freqs[x] += 1
            else:
                freqs[x] = 1


        for i in range(len(hand)):
            # start of group
            if freqs[hand[i]] > 0:
                # check can form group (j is needed number, not index)
                for j in range(hand[i], hand[i]+groupSize):
                    # print(j)
                    if j not in freqs or freqs[j] <= 0:
                        return False
                    freqs[j] -= 1


        return True