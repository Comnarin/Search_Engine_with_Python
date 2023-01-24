# This Python file uses the following encoding: utf-8
import unittest
import re
import nltk
import heapq
from keybert import KeyBERT

class TestEng(unittest.TestCase):
    def setUp(self):
        self.data = ["More classified material found at Biden's home", 'Top secret documents reportedly found in Biden cache', 'Four unanswered questions about the Biden documents', 'How Biden and Trump secret files cases compare', 'Delay in telling public about files may haunt Biden', "Republicans want to know who visited Biden's homes", 'The problem with politicians and classified files', 'Biden under investigation', 'How much trouble is the president in over classified documents found at his home?', 'Who is the special counsel in the Biden probe?', 'Special counsel appointed to investigate Biden files', 'Second batch of classified Biden documents found', 'Jill Biden has surgery to remove cancerous skin lesions', "Biden 'surprised' about classified files discovery", 'Biden visits US-Mexico border in trip to Texas', 'Western allies to send fighting vehicles to Ukraine', 'What will change with Republicans controlling the House', "What's actually in the $1.7tn US spending bill?", "Zelensky trip shows US doesn't want peace - Russia", 'Ukraine is alive and kicking, Zelensky tells US']
        self.eng = Eng(self.data)
        
    def test_get_sentence(self):
        self.assertEqual(self.eng.get_sentence(), "More classified material found at Biden's home Top secret documents reportedly found in Biden cache Four unanswered questions about the Biden documents How Biden and Trump secret files cases compare Delay in telling public about files may haunt Biden Republicans want to know who visited Biden's homes The problem with politicians and classified files Biden under investigation How much trouble is the president in over classified documents found at his home? Who is the special counsel in the Biden probe? Special counsel appointed to investigate Biden files Second batch of classified Biden documents found Jill Biden has surgery to remove cancerous skin lesions Biden 'surprised' about classified files discovery Biden visits US-Mexico border in trip to Texas Western allies to send fighting vehicles to Ukraine What will change with Republicans controlling the House What's actually in the $1.7tn US spending bill? Zelensky trip shows US doesn't want peace - Russia Ukraine is alive and kicking, Zelensky tells US")
    def test_get_tokenize(self):
        self.assertEqual(self.eng.tokenize(), ["More classified material found at Biden's home Top secret documents reportedly found in Biden cache Four unanswered questions about the Biden documents How Biden and Trump secret files cases compare Delay in telling public about files may haunt Biden Republicans want to know who visited Biden's homes The problem with politicians and classified files Biden under investigation How much trouble is the president in over classified documents found at his home?",
                    'Who is the special counsel in the Biden probe?',
                    "Special counsel appointed to investigate Biden files Second batch of classified Biden documents found Jill Biden has surgery to remove cancerous skin lesions Biden 'surprised' about classified files discovery Biden visits US-Mexico border in trip to Texas Western allies to send fighting vehicles to Ukraine What will change with Republicans controlling the House What's actually in the $1.7tn US spending bill?",
                    "Zelensky trip shows US doesn't want peace - Russia Ukraine is alive and kicking, Zelensky tells US"])  
    def test_get_keyword(self):
       self.assertEqual(self.eng.find_keyword(), [('biden', 0.4392),
                                                ('documents', 0.3501),
                                                ('classified', 0.3172),
                                                ('politicians', 0.2588),
                                                ('files', 0.2574)])
        
    def test_get_summarize(self):
        self.assertEqual(self.eng.summary_sentences(),["Zelensky trip shows US doesn't want peace - Russia Ukraine is alive and kicking, Zelensky tells US",
 'Who is the special counsel in the Biden probe?'])

class TestEng2(unittest.TestCase):
    def setUp(self):
        self.data = ['German Chancellor Olaf Scholz has decided to send Leopard 2 tanks to Ukraine, and allow other countries to do the same, reports in Germany say.', 'Leopard 2s are made in Germany and Berlin needs to approve their export.', 'Germany has been hesitant to send its own - or allow other nations to send theirs - over concerns it could escalate the conflict with Russia.', 'But now Mr Scholz has decided to send the at least a company of Leopard 2 A6 tanks, several German outlets say.', 'A company is usually 14 tanks - the same number of Leopards Poland wants to send, and the same number of Challenger 2 tanks the UK has already committed to Ukraine.', 'The news was broken by Der Spiegel in Germany, citing government sources, before being seemingly confirmed elsewhere.', 'There has been no official statement from the German government yet.', 'Ukraine sees the tanks as vital for breaking through Russian lines and to beat an anticipated Russian offensive this spring.', 'Ukraine President Volodymyr Zelensky believes about 300 Leopard tanks would help it defeat Russia.', 'Allied nations have become frustrated at what they perceive as German reluctance to send the armoured vehicles in recent days.', 'Polish PM Mateusz Morawiecki told the BBC earlier on Tuesday that Germany had a "special responsibility" to support Ukraine, having built up "huge Russian funds" before the war by buying its gas.', 'What weapons are being supplied to Ukraine?', "Germany won't block tank exports - foreign minister", 'Germany yet to commit to sending tanks to Ukraine', 'Germany to send Leopard tanks to Ukraine - reports', 'Top Ukraine officials quit in corruption crackdown', "Classified documents found at Mike Pence's home", 'Oscars 2023: The nominations in full', 'How to read the Doomsday Clock', 'Men must stand up for Afghan women - professor', 'Hero who disarmed gunman had never seen a real gun', 'Eight-year-old Indian diamond heiress who became a nun', "What you need to know about Nigeria's elections", "The Englishman who helped plot Morocco's World Cup run", "What’s the future of India's sinking Himalayan town?", 'The bacteria controlling your brain', 'The simple error that 16% of us make', "Gen Z's latest surprising obsession", 'A return to old-school Canadian glamour', '© 2023 BBC. The BBC is not responsible for the content of external sites. Read about our approach to external linking.']
        self.eng = Eng(self.data)
        
    def test_get_sentence(self):
        self.assertEqual(self.eng.get_sentence(), 'German Chancellor Olaf Scholz has decided to send Leopard 2 tanks to Ukraine, and allow other countries to do the same, reports in Germany say. Leopard 2s are made in Germany and Berlin needs to approve their export. Germany has been hesitant to send its own - or allow other nations to send theirs - over concerns it could escalate the conflict with Russia. But now Mr Scholz has decided to send the at least a company of Leopard 2 A6 tanks, several German outlets say. A company is usually 14 tanks - the same number of Leopards Poland wants to send, and the same number of Challenger 2 tanks the UK has already committed to Ukraine. The news was broken by Der Spiegel in Germany, citing government sources, before being seemingly confirmed elsewhere. There has been no official statement from the German government yet. Ukraine sees the tanks as vital for breaking through Russian lines and to beat an anticipated Russian offensive this spring. Ukraine President Volodymyr Zelensky believes about 300 Leopard tanks would help it defeat Russia. Allied nations have become frustrated at what they perceive as German reluctance to send the armoured vehicles in recent days. Polish PM Mateusz Morawiecki told the BBC earlier on Tuesday that Germany had a "special responsibility" to support Ukraine, having built up "huge Russian funds" before the war by buying its gas. What weapons are being supplied to Ukraine? Germany won\'t block tank exports - foreign minister Germany yet to commit to sending tanks to Ukraine Germany to send Leopard tanks to Ukraine - reports Top Ukraine officials quit in corruption crackdown Classified documents found at Mike Pence\'s home Oscars 2023: The nominations in full How to read the Doomsday Clock Men must stand up for Afghan women - professor Hero who disarmed gunman had never seen a real gun Eight-year-old Indian diamond heiress who became a nun What you need to know about Nigeria\'s elections The Englishman who helped plot Morocco\'s World Cup run What’s the future of India\'s sinking Himalayan town? The bacteria controlling your brain The simple error that 16% of us make Gen Z\'s latest surprising obsession A return to old-school Canadian glamour © 2023 BBC. The BBC is not responsible for the content of external sites. Read about our approach to external linking.')
    def test_get_tokenize(self):
        self.assertEqual(self.eng.tokenize(), ['German Chancellor Olaf Scholz has decided to send Leopard 2 tanks to Ukraine, and allow other countries to do the same, reports in Germany say.',
                                                    'Leopard 2s are made in Germany and Berlin needs to approve their export.',
                                                    'Germany has been hesitant to send its own - or allow other nations to send theirs - over concerns it could escalate the conflict with Russia.',
                                                    'But now Mr Scholz has decided to send the at least a company of Leopard 2 A6 tanks, several German outlets say.',
                                                    'A company is usually 14 tanks - the same number of Leopards Poland wants to send, and the same number of Challenger 2 tanks the UK has already committed to Ukraine.',
                                                    'The news was broken by Der Spiegel in Germany, citing government sources, before being seemingly confirmed elsewhere.',
                                                    'There has been no official statement from the German government yet.',
                                                    'Ukraine sees the tanks as vital for breaking through Russian lines and to beat an anticipated Russian offensive this spring.',
                                                    'Ukraine President Volodymyr Zelensky believes about 300 Leopard tanks would help it defeat Russia.',
                                                    'Allied nations have become frustrated at what they perceive as German reluctance to send the armoured vehicles in recent days.',
                                                    'Polish PM Mateusz Morawiecki told the BBC earlier on Tuesday that Germany had a "special responsibility" to support Ukraine, having built up "huge Russian funds" before the war by buying its gas.',
                                                    'What weapons are being supplied to Ukraine?',
                                                    "Germany won't block tank exports - foreign minister Germany yet to commit to sending tanks to Ukraine Germany to send Leopard tanks to Ukraine - reports Top Ukraine officials quit in corruption crackdown Classified documents found at Mike Pence's home Oscars 2023: The nominations in full How to read the Doomsday Clock Men must stand up for Afghan women - professor Hero who disarmed gunman had never seen a real gun Eight-year-old Indian diamond heiress who became a nun What you need to know about Nigeria's elections The Englishman who helped plot Morocco's World Cup run What’s the future of India's sinking Himalayan town?",
                                                    "The bacteria controlling your brain The simple error that 16% of us make Gen Z's latest surprising obsession A return to old-school Canadian glamour © 2023 BBC.",
                                                    'The BBC is not responsible for the content of external sites.',
                                                    'Read about our approach to external linking.'])
    def test_get_keyword(self):
       self.assertEqual(self.eng.find_keyword(), [('leopard', 0.4591),
                                                ('leopards', 0.4508),
                                                ('tanks', 0.4178),
                                                ('ukraine', 0.3458),
                                                ('tank', 0.3264)])
        
    def test_get_summarize(self):
        self.assertEqual(self.eng.summary_sentences(),['German Chancellor Olaf Scholz has decided to send Leopard 2 tanks to Ukraine, and allow other countries to do the same, reports in Germany say.',
 'But now Mr Scholz has decided to send the at least a company of Leopard 2 A6 tanks, several German outlets say.',
 'Germany has been hesitant to send its own - or allow other nations to send theirs - over concerns it could escalate the conflict with Russia.',
 'Allied nations have become frustrated at what they perceive as German reluctance to send the armoured vehicles in recent days.',
 'Ukraine sees the tanks as vital for breaking through Russian lines and to beat an anticipated Russian offensive this spring.'])


class Eng:
    def __init__(self,data:list):
        self.data_value = data
        self.sentence = self.get_sentence()
        
    def get_sentence(self):
        self.sentence_result = self.make_sentence(self.data_value)
        return self.sentence_result
    def make_sentence(self,list_word):
        self.sentence_value = ' '.join(list_word)
        return self.sentence_value
    def tokenize(self):
        self.sentence_list = nltk.sent_tokenize(self.sentence)
        return self.sentence_list
    def create_formatted_article(self):
        # Removing special characters and digits
        self.get_sentence()
        self.formatted_article_text = re.sub('[^a-zA-Z]', ' ', self.sentence_result )
        self.formatted_article_text = re.sub(r'\s+', ' ', self.formatted_article_text)
        return self.formatted_article_text
    def find_word_frequencies(self):
        self.tokenize()
        self.create_formatted_article()
        stopwords = nltk.corpus.stopwords.words('english')
        self.word_frequencies = {}
        for word in nltk.word_tokenize(self.formatted_article_text):
            if word not in stopwords:
                if word not in self.word_frequencies.keys():
                    self.word_frequencies[word] = 1
                else:
                    self.word_frequencies[word] += 1
        return self.word_frequencies
    def find_maximum_frequncy(self):
        self.find_word_frequencies()
        maximum_frequncy = max(self.word_frequencies.values())
        for word in self.word_frequencies.keys():
            self.word_frequencies[word] = (self.word_frequencies[word]/maximum_frequncy)
    def find_sentence_scores(self):
        self.sentence_scores = {}
        self.tokenize()
        self.find_word_frequencies()
        for sent in self.sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in self.word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in self.sentence_scores.keys():
                            self.sentence_scores[sent] = self.word_frequencies[word]
                        else:
                            self.sentence_scores[sent] += self.word_frequencies[word]
        return self.sentence_scores
    def summary_sentences(self):
        self.find_sentence_scores()
        self.summary_sentences = heapq.nlargest(5, self.sentence_scores, key=self.sentence_scores.get)
        summary = ' '.join(self.summary_sentences)
        return self.summary_sentences
    def find_keyword(self):
        self.get_sentence()
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(self.sentence_result)
        return kw_model.extract_keywords(self.sentence_result, keyphrase_ngram_range=(1, 1), stop_words=None)

if __name__ == '__main__':
    unittest.main()