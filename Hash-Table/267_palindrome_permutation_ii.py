from ast import List
from collections import Counter
from itertools import permutations

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        a = Counter(s)
        c = 0
        m = ""
        l = ""
        for i in a:
            if a[i] % 2:
                c += 1
                m = i
            l += a[i] // 2 * i
        if c > 1:
            return []
        l = list(l)
        ans = []
        s = set()
        for ll in permutations(l):
            lll = ''.join(ll)
            if lll not in s:
                s.add(lll)
                ans.append(lll + m + lll[::-1])
        return ans




# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function
data = list('123')
for p in permutation(data):
    print (p)