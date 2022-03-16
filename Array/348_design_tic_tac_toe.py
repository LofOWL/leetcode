class TicTacToe:

    def __init__(self, n: int):
        self.dic = {}
        self.dic[1] = [[0 for i in range(n)],[0 for i in range(n)],0,0]
        self.dic[2] = [[0 for i in range(n)],[0 for i in range(n)],0,0]
        self.n = n
    def move(self, row: int, col: int, player: int) -> int:
        self.dic[player][0][row] += 1
        self.dic[player][1][col] += 1
        if row == col:
            self.dic[player][2] += 1
        if row + col == self.n-1:
            self.dic[player][3] += 1
        if self.n in (self.dic[player][0][row],self.dic[player][1][col],self.dic[player][2],self.dic[player][3]):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)