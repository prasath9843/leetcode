class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0

        while i < len(words):
            j = i
            length = 0

            # Find words that fit in this line
            while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1

            count = j - i
            spaces = maxWidth - length

            # Last line or single word
            if j == len(words) or count == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                gaps = count - 1
                extra = spaces // gaps
                remainder = spaces % gaps

                line = ""

                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (extra + (1 if k < remainder else 0))

                line += words[j - 1]

            res.append(line)
            i = j

        return res