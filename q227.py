class Solution:
    def calculate(self, s: str) -> int:
        stk, operator, num, sign = [], None, 0, 1
        for c in s:
            if c.isnumeric():
                num *= 10
                num += int(c)
            elif c in "+-":
                if operator == "*": stk.append(stk.pop() * (sign * num))
                elif operator == "/": stk.append(int(stk.pop() / (sign * num)))
                else: stk.append(sign * num)

                num, operator = 0, None
                if c == "-": sign = -1
                else: sign = 1
            elif c in "*/":
                if operator == "*": stk.append(stk.pop() * (sign * num))
                elif operator == "/": stk.append(int(stk.pop() / (sign * num)))
                else: stk.append(sign * num)

                num, sign, operator = 0, 1, c

        if operator == "*": stk.append(stk.pop() * (sign * num))
        elif operator == "/": stk.append(int(stk.pop() / (sign * num)))
        else: stk.append(sign * num)
        
        res = 0
        while stk: res += stk.pop()
        return res
