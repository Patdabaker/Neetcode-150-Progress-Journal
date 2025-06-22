"""
Problem: Car Fleet
Link: https://neetcode.io/problems/car-fleet?list=neetcode150
Category: Stack
Created on: 6/18/2025

Approach:
- Gathered the pairs in both lists and sorted the tuples by position starting from largest
- Appended fleet list by time taken, and only added if current time was greater than previous time
- Returned length of the fleet list
"""
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet = []
        tuple_list = []
        for i in range(len(position)):
            tuple_list.append((position[i], speed[i]))
        tuple_list = sorted(tuple_list, reverse=True)
        for i in range(len(tuple_list)):
            time = (target - tuple_list[i][0]) / tuple_list[i][1]
            if not fleet:
                fleet.append(time)
            elif fleet and time > fleet[-1]:
                fleet.append(time)
        return len(fleet)

test = Solution()
print(test.carFleet(10, [4,1,0,7], [2,2,1,1]))
