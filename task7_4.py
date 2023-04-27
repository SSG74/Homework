import copy
class Matrix:
    #el =
    def __init__(self, my_list):
        self.my_matrix = copy.deepcopy(my_list)
    #      self.
    def __str__(self):
        string = ''
        for i in self.my_matrix:
            for j in i:
                string += '%s\t' % j
            string = string[:-1]
            string += '\n'
        string = string[:-1]
        return string
    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[0])):
                summa = other.my_matrix[i][j] + self.my_matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.my_matrix[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


M = Matrix([[1, 2, 5], [3, 4, 6]])
N = Matrix([[2, 2, 3], [3, 3, 4]])
print(M)
print(N)
print(M + N)