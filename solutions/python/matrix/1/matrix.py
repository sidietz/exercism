"""
parses a matrix
"""

class Matrix:
    """
    Matrix class
    """
    def __init__(self, matrix_string):
        lines = matrix_string.split("\n")
        matrix = []
        for line in lines:
            row = list(map(lambda x: int(x), line.split(" ")))
            matrix.append(row)

        self.matrix = matrix
            

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        columns = []
        for i, row in enumerate(self.matrix):
            columns.append(row[index-1])
        return columns
