class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)

        if endWord not in words:
            return []

        level = {beginWord}
        parents = {}
        found = False

        while level and not found:
            next_level = set()
            words -= level

            for word in level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in words:
                            next_level.add(new_word)
                            parents.setdefault(new_word, []).append(word)

                            if new_word == endWord:
                                found = True

            level = next_level

        if not found:
            return []

        res = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                res.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)
        return res