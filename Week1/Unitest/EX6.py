import unittest
from unittest.mock import patch

class AdditionTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=[2,4,'1 2 3 4','1 2 3 4','1 2 3 4','1 2 3 4',
                                            5,'2 2 2 2 2','2 2 2 2 2','2 2 2 2 2','2 2 2 2 2','2 2 2 2 2'])
    def test_sum(self, mock_inputs):
        test = sum_of_10_matrix()
        ans = test.Input()
        result = test.calculate()
        assert result ==[4,10]
        
class sum_of_10_matrix:
    def __init__(self) :
        self.Result=[]

    def Input(self):
        self.time = int(input("time : "))
        self.matrix = int(input("Matrix : "))
        self.value = input('value : ')

    def calculate(self,time,matrix,Result,value):
        def find_count(matrix_value):
                count = 0
                for m in range (matrix):
                    row = matrix_value[m]
                    total = 0
                    for j in range(len(row)) :
                        if total == 10:
                                count +=1
                        total = 0
                        
                        for i in range(j,len(row)):
                            if total == 10:
                                count +=1
                                total = 0
                            elif total < 10:
                                total+=row[i]
                return count
        for i in range(time):
            matrix = int(input("Matrix : "))
            value = []

            for j in range(matrix):
                value += value.split()

            list_of_integers = [int(item) for item in value]
            rows = []
            rows_size = matrix

            for i in range(0, len(list_of_integers), rows_size):
                rows.append(list_of_integers[i:i+rows_size])
            n = matrix 
            columns = []

            for i in range(n):
                column = []
                for j in range(n):
                    column.append(rows[j][i])
                columns.append(column)
                    
            Result.append(find_count(rows)+find_count(columns))