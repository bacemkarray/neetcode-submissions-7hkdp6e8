class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        bArrayRow = [False] * len(matrix)
        bArrayCol = [False] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    bArrayRow[i] = True
                    bArrayCol[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if bArrayCol[j] or bArrayRow[i]:
                    matrix[i][j] = 0