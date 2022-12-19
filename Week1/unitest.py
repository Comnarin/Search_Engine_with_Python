import unittest

class Check_repeat_TestCase(unittest.TestCase):
    def test_main(self):
        result = check_repeat([1,2,3,4,5,6,1,2,7,8,9,7,9])
        assert result == [1, 2, 7, 9]

    def test_threeargs(self):
        result = check_repeat([1,2,3,4,5,6,7,8])
        assert result == []

    def test_noargs(self):
        result = check_repeat([])
        assert result == []


def check_repeat(array):
    check_duplicate=[]
    duplicate=[]
    for i in range (len(array)):
        if array[i] in check_duplicate:
            duplicate.append(array[i])
        else:
            check_duplicate.append(array[i])
    return(duplicate)


if __name__ == "__main__":
    unittest.main()




