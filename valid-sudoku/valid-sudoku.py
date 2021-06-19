class Solution:
    def isValidSudoku(self, board):
        for i in range(len(board)):
            board[i] = list(map(lambda x: int(x) if x.isdigit() else 0, board[i]))
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != 0:
                    if item in rows[i]:
                        return False
                    else:
                        rows[i].add(item)

                    if item in cols[j]:
                        return False
                    else:
                        cols[j].add(item)

                    if 0 <= i < 3 and 0 <= j < 3:
                        if item in squares[0]:
                            return False
                        squares[0].add(item)
                    elif 0 <= i < 3 and 3 <= j < 6:
                        if item in squares[1]:
                            return False
                        squares[1].add(item)
                    elif 0 <= i < 3 and 6 <= j < 9:
                        if item in squares[2]:
                            return False
                        squares[2].add(item)
                    elif 3 <= i < 6 and 0 <= j < 3:
                        if item in squares[3]:
                            return False
                        squares[3].add(item)
                    elif 3 <= i < 6 and 3 <= j < 6:
                        if item in squares[4]:
                            return False
                        squares[4].add(item)
                    elif 3 <= i < 6 and 6 <= j < 9:
                        if item in squares[5]:
                            return False
                        squares[5].add(item)
                    elif 6 <= i < 9 and 0 <= j < 3:
                        if item in squares[6]:
                            return False
                        squares[6].add(item)
                    elif 6 <= i < 9 and 3 <= j < 6:
                        if item in squares[7]:
                            return False
                        squares[7].add(item)
                    elif 6 <= i < 9 and 6 <= j < 9:
                        if item in squares[8]:
                            return False
                        squares[8].add(item)
        return True