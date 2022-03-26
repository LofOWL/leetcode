from ast import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []
        res = []
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        for i, c in enumerate(p):
            p_cnt[ord(c) - 97] += 1
            s_cnt[ord(s[i]) - 97] += 1
        if p_cnt == s_cnt:
            res.append(0)
        for i in range(len_s - len_p):
            s_cnt[ord(s[i]) - 97] -= 1
            s_cnt[ord(s[i + len_p]) - 97] += 1
            if s_cnt == p_cnt:
                res.append(i + 1)
        return res