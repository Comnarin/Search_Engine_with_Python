import unittest
import spacy

class TestSpacyProcessor(unittest.TestCase):
    def setUp(self):
        self.EnglishNLP = SpacyProcessor()
        
    def test_process(self):
        text = "This is a sample sentence."
        expected_output = ['sample', 'sentence']
        self.assertEqual(self.EnglishNLP.process(text), expected_output)

    def test_Remove_punctuations(self): 
        text = "Hello, how are you doing today?"
        expected_output = ['hello', 'today']
        self.assertEqual(self.EnglishNLP.process(text), expected_output)
    def test_base_verb(self):  
        text = "I'm not feeling very well."
        expected_output = ['feel']
        self.assertEqual(self.EnglishNLP.process(text), expected_output)
    def test_full_sentence(self):
        text = "Jeng is eating friedrice and Ping is eating noodle and Moss has ate apple"
        expected_output = ['Jeng', 'eat', 'friedrice', 'Ping', 'eat', 'noodle', 'Moss', 'eat', 'apple']
        self.assertEqual(self.EnglishNLP.process(text), expected_output)

        text = "Narin Sirinapuk is studying Software Development."
        expected_output = ['Narin', 'Sirinapuk', 'study', 'Software', 'Development']
        self.assertEqual(self.EnglishNLP.process(text), expected_output)

class SpacyProcessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        
    def process(self, text):
        doc = self.nlp(text)
        
        # Tokenization and lemmatization 
        lemma_list = []
        for token in doc:
            lemma_list.append(token.lemma_)
        
        # Filter the stopword
        filtered_sentence =[] 
        for word in lemma_list:
            lexeme = self.nlp.vocab[word]
            if lexeme.is_stop == False:
                filtered_sentence.append(word) 

        # Remove punctuation
        punctuations="?:!.,;"
        filtered_sentence = [word for word in filtered_sentence if word not in punctuations]

        return filtered_sentence

if __name__ == '__main__':
    unittest.main()
