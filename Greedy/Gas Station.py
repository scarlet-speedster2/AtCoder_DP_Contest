'''
    Intuation: You can reach to the station Y form any station between X --- Y-1 if the
                station in unreachable form X
                so we can start directly form station Y next time
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = - 1
        N = len(gas)
        s = 0
        i = 0
        unreachable = -1
        while i < N:

            start = i
            val = 0
            while True:
                val += gas[start]
                new_index = (start + 1) % N
                if new_index == i and val - cost[start] >= 0:
                    return i
                if val - cost[start] < 0:
                    unreachable = new_index
                    break
                val -= cost[start]
                start = new_index
            if unreachable <= i:
                return -1
            i = unreachable
        return ans

