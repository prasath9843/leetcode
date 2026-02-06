from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)                     # Count frequency
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        result = ""
        for ch, count in sorted_chars:
            result += ch * count
        
        return result
