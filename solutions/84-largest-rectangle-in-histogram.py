from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        heights.append(0)
        for i in range(len(heights)):
            j = i
            while stack != [] and stack[-1][1] > heights[i]:
                popped = stack.pop()
                j = popped[0]
                area = (i - j) * popped[1]
                res = max(area, res)
                print(stack, res)
            stack.append((j, heights[i]))
            print(stack)

        return res

if __name__ == "__main__":
    print(Solution.largestRectangleArea(None, [7,1,7,2,2,4]))
