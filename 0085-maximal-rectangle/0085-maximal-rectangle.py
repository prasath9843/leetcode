class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:
            for j in range(n):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    ans = max(ans, height * width)
                stack.append(i)

        return ans