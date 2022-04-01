"""
字典，v是字母i是index，对于已有v， 新的i会覆盖旧的
一路滑过去，如果没有遇到不同的数量超k情况，最后就是len(s)-srt
遇到了的话，那就是刚好大一个的情况，所以是k要加一的情况。
记录一下之前的子数组长度 max(i - srt, res)， 不用+1是因为这个i本来就大一位，应该选上个i，上个i+1就是这个i嘛。 x是最小的index，满足条件的，（不同的字母的）位置（来了个新的不同字母把旧的最小位挤走了）。因为一个一个去除首项到头来还是得到这一位。
新的首项就是x+1.

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0: return 0
        has, res, srt = {}, 0, 0
        for i,v in enumerate(s):
            has[v] = i
            if len(has) == k+1:
                res, x = max(i - srt, res), min(has.values())
                del has[s[x]]
                srt = x + 1
        return max(res, len(s)-srt)
