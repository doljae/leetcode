class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        height, width = len(mat), len(mat[0])
        new_mat = [[0] * (width + 2 * k) for _ in range(height + 2 * k)]
        answer = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                new_mat[i + k][j + k] = mat[i][j]

        # for item in new_mat:
        #     print(item)

        height2, width2 = height + 2 * k, width + 2 * k
        for i in range(1, height2):
            for j in range(1, width2):
                new_mat[i][j] += new_mat[i][j - 1]

        for j in range(1, width2):
            for i in range(1, height2):
                new_mat[i][j] += new_mat[i - 1][j]

        # for item in new_mat:
        #     print(item)
        # print()

        def sol(x1, y1, x2, y2):
            # print(x1, y1, x2, y2)
            result = new_mat[x2][y2]
            a = new_mat[x2][y1 - 1] if y1 - 1 >= 0 else 0
            b = new_mat[x1 - 1][y2] if x1 - 1 >= 0 else 0
            c = new_mat[x1 - 1][y1 - 1] if x1 - 1 >= 0 and y1 - 1 >= 0 else 0
            # print(result, a, b, c)
            return result - a - b + c

        for i in range(height):
            for j in range(width):
                x1, y1 = i, j
                x2, y2 = i + 2 * k, j + 2 * k
                answer[i][j] = sol(x1, y1, x2, y2)
            # print()

        # for item in answer:
        #     print(item)
        
        return answer