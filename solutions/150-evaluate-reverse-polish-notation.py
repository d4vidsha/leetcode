from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-/*"
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "/":
                    stack.append(int(l / r))
                elif t == "*":
                    stack.append(l * r)
        return stack.pop()

if __name__ == "__main__":
    print(Solution.evalRPN(None, ["1","2","+","3","*","4","-"]))
