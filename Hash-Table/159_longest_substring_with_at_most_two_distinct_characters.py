class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if (len(s) < 2):
            return len(s)
        else:
            length = len(s)
            firstChar = s[0]
            firstIndex = 0
            index = 1
            while (index < length and s[index] == firstChar):
                index += 1
                firstIndex += 1
            if (index == length):
                return len(s)
            else:
                secondChar = s[index]
                secondIndex = index
                maxLen = index + 1
                curLen = maxLen
                index += 1
                while (index < length):
                    char = s[index]
                    if (char != firstChar and char != secondChar):
                        curLen = index - firstIndex
                        firstChar = secondChar
                        firstIndex = secondIndex
                        secondChar = char
                        secondIndex = index
                    elif (char == firstChar):
                        temp = firstChar
                        firstChar = secondChar
                        secondChar = temp
                        firstIndex = secondIndex
                        secondIndex = index
                        curLen += 1
                    else:
                        secondIndex = index
                        curLen += 1
                    if (curLen > maxLen):
                        maxLen = curLen
                    # print(index, firstChar, secondChar)
                    # print(curLen, maxLen)
                    index += 1
                return maxLen

