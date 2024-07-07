from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort(key=lambda x: x[0])

        for i in range(len(position)-1, -1, -1):
            car = pairs[i]
            time = (target - car[0]) / car[1]
            if stack == []:
                stack.append(time)
                continue
            if stack[-1] < time:
                stack.append(time)

        return len(stack)


if __name__ == "__main__":
    print(Solution.carFleet(None, 10, [1,4], [3,2]))
