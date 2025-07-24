class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            a=word.index(ch)
            b=word[a::-1]+word[a+1::]
            return b
        else:
            return word
        