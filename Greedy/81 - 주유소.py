# https://leetcode.com/problems/gas-station/submissions/

#

# 브루트 포스
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for start in range(len(gas)):
            fuel = 0
            flag = True
            for i in range(start, start + len(gas)):
                index = i % len(gas)

                if gas[index] + fuel < cost[index]:
                    flag = False
                    break

                fuel += gas[index] - cost[index]

            if flag:
                return start

        return -1