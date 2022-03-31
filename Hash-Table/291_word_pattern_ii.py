class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def matchNextWord(i, j):
            if i == n:
                return j == len(s)

            if pattern[i] in dict1:
                if dict1[pattern[i]] != s[j:j + len(dict1[pattern[i]])]:
                    return False
                return matchNextWord(i + 1, j + len(dict1[pattern[i]]))

            for l in range(1, len(s) - j + 1):
                if s[j:j + l] in words:
                    continue
                dict1[pattern[i]] = s[j:j + l]
                words.add(s[j:j + l])
                if matchNextWord(i + 1, j + l):
                    return True
                dict1.pop(pattern[i])
                words.remove(s[j:j + l])
            return False            

        n = len(pattern)
        dict1 = {}
        words = set()
        return matchNextWord(0, 0)