class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i, ch in enumerate(s + '+'):
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch != ' ':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)

                sign = ch
                num = 0

        return sum(stack)