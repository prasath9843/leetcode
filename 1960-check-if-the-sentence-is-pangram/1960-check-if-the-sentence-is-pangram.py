class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            if (chr(97+i)) not in sentence:
                return False
        return True
        