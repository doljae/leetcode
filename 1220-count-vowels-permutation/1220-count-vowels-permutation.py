class Solution:
    def countVowelPermutation(self, n: int) -> int:
        board = [[0] * 5 for _ in range(n + 1)]
        modulo = pow(10, 9) + 7
        A, E, I, O, U = 0, 1, 2, 3, 4
        index_map = {A: [E],
                     E: [A, I],
                     I: [A, E, O, U],
                     O: [I, U],
                     U: [A]}

        for i in range(1, len(board)):
            for j in range(len(board[0])):
                if i == 1:
                    board[i][j] = 1
                else:
                    board[i][j] += sum(list(map(lambda x: board[i - 1][x], index_map[j]))) % modulo

        return sum(board[n]) % modulo