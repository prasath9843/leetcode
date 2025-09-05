class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check for sign
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # Step 3: Read digits
        num = 0
        for ch in s:
            if not ch.isdigit():
                break
            num = num * 10 + int(ch)

        # Step 4: Apply sign
        num *= sign

        # Step 5: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
