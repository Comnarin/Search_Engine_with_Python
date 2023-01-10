# This Python file uses the following encoding: utf-8
import unittest
import pythainlp.util
from pythainlp.tokenize import word_tokenize
from pythainlp.util import find_keyword
from pythainlp.summarize import summarize

class TestThai(unittest.TestCase):
    def setUp(self):
        self.data = ['การทำเกษตรกรรมในปัจจุบันต้องยอมรับว่า “มีการนำสารเคมี และยากำจัดศัตรูพืช” เข้ามาใช้ประโยชน์อย่างแพร่หลาย “เพื่อช่วยเพิ่มปริมาณผลผลิตและทางกายภาพที่สวยงาม” ให้สามารถจำหน่ายแข่งขันในท้องตลาดได้ ทำให้มีการนำเข้าสารเคมีกลุ่มนี้ปริมาณสูงขึ้นอย่างต่อเนื่องทุกปี', 'กลายเป็นว่า “สารเคมีเหล่านี้ตกค้างในสิ่งแวดล้อมและผลผลิต” ส่งผลกระทบเป็นอันตรายต่อสุขภาพคนไทยจากการรับประทานอาหารปนเปื้อนเข้าสู่ร่างกาย ทำให้ในช่วงที่ผ่านมามีการเรียกร้องให้ยกเลิกการใช้สารพาราควอต ไกลโฟเซต และคลอร์ไพริฟอส เพื่อให้เกิดความปลอดภัยในการบริโภคผลิตผลทางการเกษตรนั้น', 'แล้วไม่นานมานี้ Thai Climate Justice for All ร่วมกับสมัชชาองค์กรเอกชนด้านการคุ้มครองสิ่งแวดล้อมและอนุรักษ์ทรัพยากร และศูนย์มานุษยวิทยาสิรินธร (องค์การมหาชน) จัดเวที Ted Talk Climate Change สิ่งแวดล้อมประจำปี 2565 จากมุมมองนักเคลื่อนไหวภาคประชาสังคม และนักวิชาการทำงานกับประชาชนแต่ละด้าน']
        self.thai = Thai(self.data)
        
    def test_get_sentence(self):
        self.assertEqual(self.thai.sentence, 'การทำเกษตรกรรมในปัจจุบันต้องยอมรับว่า “มีการนำสารเคมี และยากำจัดศัตรูพืช” เข้ามาใช้ประโยชน์อย่างแพร่หลาย “เพื่อช่วยเพิ่มปริมาณผลผลิตและทางกายภาพที่สวยงาม” ให้สามารถจำหน่ายแข่งขันในท้องตลาดได้ ทำให้มีการนำเข้าสารเคมีกลุ่มนี้ปริมาณสูงขึ้นอย่างต่อเนื่องทุกปี กลายเป็นว่า “สารเคมีเหล่านี้ตกค้างในสิ่งแวดล้อมและผลผลิต” ส่งผลกระทบเป็นอันตรายต่อสุขภาพคนไทยจากการรับประทานอาหารปนเปื้อนเข้าสู่ร่างกาย ทำให้ในช่วงที่ผ่านมามีการเรียกร้องให้ยกเลิกการใช้สารพาราควอต ไกลโฟเซต และคลอร์ไพริฟอส เพื่อให้เกิดความปลอดภัยในการบริโภคผลิตผลทางการเกษตรนั้น แล้วไม่นานมานี้ Thai Climate Justice for All ร่วมกับสมัชชาองค์กรเอกชนด้านการคุ้มครองสิ่งแวดล้อมและอนุรักษ์ทรัพยากร และศูนย์มานุษยวิทยาสิรินธร (องค์การมหาชน) จัดเวที Ted Talk Climate Change สิ่งแวดล้อมประจำปี 2565 จากมุมมองนักเคลื่อนไหวภาคประชาสังคม และนักวิชาการทำงานกับประชาชนแต่ละด้าน')
        
    def test_get_keyword(self):
       self.assertEqual(self.thai.keyword, {})
        
    def test_get_summarize(self):
        self.assertEqual(self.thai.summarize,['ส่งผลกระทบเป็นอันตรายต่อสุขภาพคนไทยจากการรับประทานอาหารปนเปื้อนเข้าสู่ร่างกาย',
 'ทำให้ในช่วงที่ผ่านมามีการเรียกร้องให้ยกเลิกการใช้สารพาราควอต',
 'ร่วมกับสมัชชาองค์กรเอกชนด้านการคุ้มครองสิ่งแวดล้อมและอนุรักษ์ทรัพยากร',
 '“เพื่อช่วยเพิ่มปริมาณผลผลิตและทางกายภาพที่สวยงาม”',
 'และคลอร์ไพริฟอส',
 'ทำให้มีการนำเข้าสารเคมีกลุ่มนี้ปริมาณสูงขึ้นอย่างต่อเนื่องทุกปี',
 'เพื่อให้เกิดความปลอดภัยในการบริโภคผลิตผลทางการเกษตรนั้น',
 'จากมุมมองนักเคลื่อนไหวภาคประชาสังคม',
 'และยากำจัดศัตรูพืช”',
 'เข้ามาใช้ประโยชน์อย่างแพร่หลาย'])

class Thai:
    def __init__(self,data:list):
        self.data_value = data
        self.sentence = self.get_sentence()
        self.keyword = self.get_keyword()
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
    def get_keyword(self):
        self.keyword_result = {}
        self.keyword_value = word_tokenize(self.sentence, engine="newmm")
        self.keyword_dict = find_keyword(self.keyword_value)
        # Iterate over the keys in the dictionary
        for key in self.keyword_dict:
        # Check if the key is text (i.e., not a space or quotation mark)
            if key.isalpha():
            # If the key is text, add it to the new dictionary
                self.keyword_result[key] = self.keyword_dict[key]
        return self.keyword_result
    def get_summarize(self):
        self.summarize_result =[]
        self.summarize_result = summarize(self.sentence,n=10)
        return self.summarize_result

if __name__ == '__main__':
    unittest.main()