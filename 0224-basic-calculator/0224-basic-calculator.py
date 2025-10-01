class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 for +, -1 for -
        res = 0

        for c in s + '+':  # add dummy + to process last number
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                # push current result and sign
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()  # sign before parentheses
                res += stack.pop()  # previous result
        return res 