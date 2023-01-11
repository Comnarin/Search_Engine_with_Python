# This Python file uses the following encoding: utf-8
import unittest
from unittest.mock import patch
import pythainlp.util
from pythainlp.tokenize import word_tokenize
from pythainlp.util import find_keyword
from pythainlp.summarize import summarize

class AdditionTestCase(unittest.TestCase):
    @patch('builtins.input',side_effect=['Nattavee','Narischat'])
    def test_sentence(self, mock_inputs):
        test = Thai(mock_inputs)
        result = test.get_sentence()
        assert result == 'Narischat'
    
''' @patch('builtins.input',side_effect=[1,2,'1 2','1 2 '])
    def test_noAnswer(self, mock_inputs):
        test = sum_of_10_matrix()
        result = test.Input()
        result = test.calculator()
        assert result == [0]
    
    @patch('builtins.input',side_effect=[1,1,'1'])
    def test_1metrix(self, mock_inputs):
        test = sum_of_10_matrix()
        result = test.Input()
        result = test.calculator()
        assert result == [0]
    
    @patch('builtins.input',side_effect=[0])
    def test_0metrix(self, mock_inputs):
        test = sum_of_10_matrix()
        result = test.Input()
        result = test.calculator()
        assert result == []'''

   
        
class Thai:
    def __init__(self,data:list):
        self.data_value = data
        self.sentence = self.get_sentence()
        #self.keyword = self.get_keyword()
        self.summarize = self.get_summarize()
    def make_sentence(self,list_word):
        self.sentence_value = ''
        for i in list_word:
            for i in list_word:
                if pythainlp.util.countthai(i)<30:
                    list_word.remove(i)
        self.sentence_value = ' '.join(list_word)
        return self.sentence_value
    def get_sentence(self):
        self.sentence_result = self.make_sentence(self.data_value)
        return self.sentence_result
    '''def get_keyword(self):
        self.keyword_result = {}
        self.keyword_value = word_tokenize(self.sentence, engine="newmm")
        self.keyword_dict = find_keyword(self.keyword_value)
        # Iterate over the keys in the dictionary
        for key in self.keyword_dict:
        # Check if the key is text (i.e., not a space or quotation mark)
            if key.isalpha():
            # If the key is text, add it to the new dictionary
                self.keyword_result[key] = self.keyword_dict[key]
        return self.keyword_result'''
    def get_summarize(self):
        self.summarize_result =[]
        self.summarize_result = summarize(self.sentence,n=10)
        return self.summarize_result

if __name__ == "__main__":
    unittest.main()