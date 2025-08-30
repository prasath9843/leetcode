from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        result = []

        for i in range(word_len):  
            left = i
            count = 0
            seen = {}

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_map:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result
