import collections
import itertools

class Solution:
    def exist(self, board, word):
        def backtracking(r, c, step=0):
            if step == len(word):  return True
            if 0 <= r < m and 0 <= c < n and board[r][c] == word[~step] and (
                    r, c) not in visited:
                visited.add((r, c))
                HashMap[(r, c, step)] += 1
                for nr, nc in (r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c):
                    if HashMap[(nr, nc, step + 1)] < n:
                        if backtracking(nr, nc, step + 1):
                            return True
                visited.remove((r, c))
                return False

        m, n = len(board), len(board[0])
        visited, HashMap = set(), collections.defaultdict(int)
        for i, j in itertools.product(range(m), range(n)):
            if backtracking(i, j):
                return True
        return False
