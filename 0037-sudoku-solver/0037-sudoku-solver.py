class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    n = int(board[r][c]) - 1
                    bit = 1 << n
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def solve():
            if not empty:
                return True

            # Find the empty cell with minimum choices
            best = -1
            best_mask = 0
            min_count = 10

            for i, (r, c) in enumerate(empty):
                b = (r // 3) * 3 + c // 3
                mask = ~(rows[r] | cols[c] | boxes[b]) & 511
                count = mask.bit_count()

                if count < min_count:
                    min_count = count
                    best = i
                    best_mask = mask

                    if count == 1:
                        break

            if best == -1:
                return True

            r, c = empty.pop(best)
            b = (r // 3) * 3 + c // 3

            while best_mask:
                bit = best_mask & -best_mask
                best_mask -= bit

                n = bit.bit_length()
                board[r][c] = str(n)

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if solve():
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            board[r][c] = "."
            empty.insert(best, (r, c))
            return False

        solve()