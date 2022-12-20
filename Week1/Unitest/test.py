import unittest
from unittest.mock import patch, mock_open




class TestReadFiles(unittest.TestCase):
    def test_count_lines(self):
        file_content_mock = """Hello World!!
Hello World is in a file.
A mocked file.
He is not real.
But he think he is.
He doesn't know he is mocked"""
        

        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)
class FileReader:

    @staticmethod
    def count_lines(file_path):
        with open(file_path, 'r') as _file:
            file_content_list = _file.readlines()
            print(file_content_list)
            return len(file_content_list)

if __name__ == "__main__":
    unittest.main()