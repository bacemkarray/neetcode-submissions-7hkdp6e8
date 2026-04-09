class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        if sum(diff) < 0:
            return -1

        amount = 0
        index = 0
        for i in range(len(gas)):
            amount += (gas[i]-cost[i])
            if amount < 0:
                amount = 0
                index = i+1
            
            
        return index

        
        