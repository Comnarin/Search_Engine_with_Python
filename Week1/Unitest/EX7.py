#"""16 200 -10 12 70 1 999 50 20 1000 150 300 200 90 900 40 140 130 30"""
import unittest
from unittest.mock import patch, mock_open
with patch("builtins.open", mock_open(read_data="""16 200 -10 12 70 1 999 50 20 1000 150 300 200 90 900 40 140 130 30""")) as mock_file:
    assert open("path/to/open").read() == """16 200 -10 12 70 1 999 50 20 1000 150 300 200 90 900 40 140 130 30"""
mock_file.assert_called_with("path/to/open")
@patch("builtins.open", new_callable=mock_open, read_data="""16 200 -10 12 70 1 999 50 20 1000 150 300 200 90 900 40 140 130 30""")
def test_patch(mock_file):
    test = solve()
    result = test.readfile(mock_file)
    result = test.calculate(mock_file)
    assert result == """16 200 -10 12 70 1 999 50 20 1000 150 300 200 90 900 40 140 130 30"""
    mock_file.assert_called_with("path/to/open")
#Ex7
def solve():
    def readfile(input_file):
        lines = []
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                lines.append(line)
        return(lines)

    def calculate(lines):
        x1,x2,x3,x4,x5,x6,x7,x8 = int,int,int,int,int,int,int,int
        c_values=lines[1:3]
        x_values=lines[3:]
        for i in range(0 ,len(c_values)):
            c_values[i] = int(c_values[i])
        for i in range(0 ,len(x_values)):
            x_values[i] = int(x_values[i])
        x_values = set(x_values)
        c1 = c_values[0]
        c2 = c_values[1]
        for x1 in x_values:
            for x2 in x_values:
                if x2 != x1 and x1 + x2 == c1:
                    x3_values = [x3 for x3 in x_values if x3 not in {x1, x2}]
                    for x3 in x3_values:
                        x4_values = [x4 for x4 in x_values if x4 not in {x1, x2, x3}]
                        for x4 in x4_values:
                            if x4 == x3 + x1:
                                x5_values = [x5 for x5 in x_values if x5 not in {x1, x2, x3, x4}]
                                for x5 in x5_values:
                                    x6_values = [x6 for x6 in x_values if x6 not in {x1, x2, x3, x4, x5}]
                                    for x6 in x6_values:
                                        x7_values = [x7 for x7 in x_values if x7 not in {x1, x2, x3, x4, x5, x6}]
                                        for x7 in x7_values:
                                            x8_values = [x8 for x8 in x_values if x8 not in {x1, x2, x3, x4, x5, x6, x7}]
                                            for x8 in x8_values:
                                                if x8 - x6 == c2 and x7 == x5 + x6:
                                                    return(x1,x2,x3,x4,x5,x6,x7,x8)   


if __name__ == "__main__":
    unittest.main()