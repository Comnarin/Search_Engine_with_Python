import unittest
from unittest.mock import patch

class AdditionTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=[2,4,'1 2 3 4','1 2 3 4','1 2 3 4','1 2 3 4',
                                            5,'2 2 2 2 2','2 2 2 2 2','2 2 2 2 2','2 2 2 2 2','2 2 2 2 2'])
    def test_sum(self, mock_inputs):
        test = sum_of_10_matrix()
        result = test.Input()
        assert result == [4,10]
        
class sum_of_10_matrix():
    def __init__(self) :
        self.matrix = []
        self.Input = []
    def Input(self):
        self.time = int(input("time : "))
        self.size = []
        self.data_rows = []
        self.data_columns =[]
        time = int(input("time : "))
        for i in range(time):
            matrix = int(input("Matrix : "))
            self.size.append(matrix)
            value =[]
            for i in range(self.size[i]):
                value += input('value : ').split()
            
            list_of_integers = [int(item) for item in value]
            rows =[]
            for i in range(0, len(list_of_integers),self.size[-1]):
                rows.append(list_of_integers[i:i+self.size[-1]])
            
            self.data_rows.append(rows)
    
            columns = []
            for i in range(self.size[-1]):
                column = []
                for j in range(self.size[-1]):
                    column.append(rows[j][i])
                columns.append(column)
            self.data_columns.append(columns)
        return self.data_rows,self.data_columns
        
    def find_count(matrix_value,size):
            count = 0
            for m in range (size):
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
                
    def calculator(self):
        for i in self.size:
            Result += (self.find_count(self.data_rows[i],self.size[i])+self.find_count(self.data_columns[i],self.size[i]))
        return Result

if __name__ == "__main__":
    unittest.main()