import unittest
class Check_triple_TestCase(unittest.TestCase):
    def test_main(self):
        result = findtriple([0,-1,-2,-3,1,2,-4,4,3])
        assert result == [{0, 1, -1}, {0, 2, -2}, {0, -4, 4}, {0, 3, -3}, {4, -3, -1}, {3, -2, -1}, {1, 2, -3}, {1, 3, -4}]
    
    def test_noTriplet(self):
        result = findtriple([1,2,3,4,5,6,7])
        assert result == "No_Triplet_Found"
    
    def test_main(self):
        result = findtriple([0,-1])
        assert result == "Input atleast 3 numbers"

    def test_noargs(self):
        result = findtriple('a')
        assert result == "Invalid Array Type"

def findtriple(array):
    Result =""
    found = False
    l=[]
    if type(array) != list:
        return("Invalid Array Type")
    if len(array) < 3:
        return("Input atleast 3 numbers")

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
        Result = "No_Triplet_Found"
    else:
        Result = l
    return Result
    
if __name__ == "__main__":
    unittest.main()