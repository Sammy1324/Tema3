from matrix import Matrix

class Launcher:
    def recursive_det(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix [1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for c in range(len(matrix)):
            
            sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            sign = (-1)**c
            det += sign * matrix[0][c] * self.recursive_det(sub_matrix)
        return det

    def iterative_det(self, matrix):
        n = len(matrix)
        det = 1
        for i in range(n):
            for j in range(i + 1, n):
                if matrix[j][i] == 0:
                    continue
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]
        for i in range(n):
            det *= matrix[i][i]
        return det
    
    def main(self):
        m = Matrix(3, 3)
        matrix = m.data
        print("Determinante (recursivo):", self.recursive_det(matrix))
        print("Determinante (iterativo):", self.iterative_det(matrix))