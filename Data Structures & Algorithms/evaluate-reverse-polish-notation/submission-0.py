class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:

            if ch not in {"+", "-", "*", "/"}:
                stack.append(int(ch))
            
            elif ch == "+":
                add1 = stack.pop()
                add2 = stack.pop()

                add = add1 + add2
                stack.append(add)
            elif ch == "*":
                mul1 = stack.pop()
                mul2 = stack.pop()

                mul = mul1 * mul2
                stack.append(mul)
            elif ch == "-":
                sub1 = stack.pop()
                sub2 = stack.pop()

                sub = sub2 - sub1
                stack.append(sub)

            elif ch == "/":
                div1 = stack.pop()
                div2 = stack.pop()

                div = int(div2 / div1)
                stack.append(div)
        return stack[-1]


        