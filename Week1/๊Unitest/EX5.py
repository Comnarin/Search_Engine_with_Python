import unittest
class Check_triple_TestCase(unittest.TestCase):
    def test_main(self):
        result = findtriple([0,-1,-2,-3,1,2,-4,4,3])
        assert result == [{0, 1, -1}, {0, 2, -2}, {0, -4, 4}, {0, 3, -3}, {4, -3, -1}, {3, -2, -1}, {1, 2, -3}, {1, 3, -4}]
    def test_threeargs(self):
        result = findtriple([1,2,3,4,5,6,7])
        assert result == 'No Triplet Found'

    def test_noargs(self):
        result = findtriple([])
        assert result == 'No Triplet Found'

def findtriple(array):
    found = False
    l=[]
    for i in range(len(array) - 1):
        s = set()
        for j in range(i + 1, len(array)):
            x = -(array[i] + array[j])
            if x in s:
                tripleset=set()
                tripleset.add(x)
                tripleset.add(array[i])
                tripleset.add(array[j])
                l.append(tripleset)
                found = True
            else:
                s.add(array[j])
    if found == False:
        print("No Triplet Found")
    else:
        print(l)
if __name__ == "__main__":
    unittest.main()