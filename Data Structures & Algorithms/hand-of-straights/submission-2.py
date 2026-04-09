class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        freq = {}

        for i in hand:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        hand.sort()
        for num in hand:
            if freq[num]:
                for i in range(num,num+groupSize):
                    if not freq.get(i,0):
                        return False
                    freq[i] -= 1
        return True
