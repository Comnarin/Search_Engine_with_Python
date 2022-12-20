import unittest
class Check_repeat_TestCase(unittest.TestCase):
    def test_main(self):
        result = findDuplicates([1,2,3,4,5,6,1,2,7,8,9,7,9,1,2,4,2,2])
        assert result == {
            1: {'count': 2, 'indices': [6, 13]},
            2: {'count': 4, 'indices': [7, 14, 16, 17]},
            7: {'count': 1, 'indices': [11]},9: {'count': 1, 'indices': [12]},
            4: {'count': 1, 'indices': [15]}
            }

    def test_threeargs(self):
        result = findDuplicates([1,2,3,4,5,6,7,8])
        assert result == {}

    def test_noargs(self):
        result = findDuplicates(a)
        assert result == {}

def findDuplicates(array):
    Table = {}
    duplicates = {}
    try:
        if not isinstance(array, list):
            raise TypeError("Invalid Array Type")
    except TypeError as error:
        print(error)

    for i in range(0, len(array)):
        if array[i] in Table:
            if array[i] in duplicates:
                duplicates[array[i]]["count"] += 1
                duplicates[array[i]]["indices"].append(i)
            else: 
                duplicates[array[i]] = {"count": 1, "indices": [i]}
        else:
            Table[array[i]] = True
    return duplicates

array=[1,2,3,4,5,6,1,2,7,8,9,7,9,1,2,4,2,2]

if __name__ == "__main__":
    unittest.main()
