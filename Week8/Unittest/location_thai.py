# This Python file uses the following encoding: utf-8
import unittest
import unicodedata
import pythainlp.util
from pythainlp.tokenize import word_tokenize
from pythainlp.util import find_keyword
from pythainlp.summarize import summarize
from pythainlp.tag import tag_provinces

class location1(unittest.TestCase):
    def setUp(self):
        self.data_loadout = ['นาทีเรือบรรทุกน้ํามันเตา โซลาร์ระเบิดสนั่นทั้งเมืองแม่กลอง แรงสั่นสะเทือนไปไกลถึงอ.บางคนที พบศพเป็นชายขาดครึ่งท่อน และอีกศพอยู่ใต้ท้องเรือ มีผู้สูญหายอีก 7 เสียงปะทุยังดังเป็นระยะ ยังมีน้ํามันเหลือค้างอยู่ในท้องเรือหลายหมื่นลิตรนาทีเรือบรรทุกน้ํามันเตา โซลาร์ระเบิดสนั่นทั้งเมืองแม่กลอง แรงสั่นสะเทือนไปไกลถึงอ.บางคนที พบศพเป็นชายขาดครึ่งท่อน และอีกศพอยู่ใต้ท้องเรือ มีผู้สูญหายอีก 7 เสียงปะทุยังดังเป็นระยะ ยังมีน้ํามันเหลือค้างอยู่ในท้องเรือหลายหมื่นลิตรโดยมีเสียงระเบิดดังสนั่น 2 ครั้งติดต่อกัน แรงสั่นสะเทือนไปไกลถึง อ.บางคนที ทําให้กระจกบ้านเรือนบริเวณนั้นแตกกระจาย แรงระเบิดส่งให้ปล่องเรือกระเด็นขึ้นฝั่งขาดเป็น 2 ท่อน พนักงานนั่งทํางานหน้าอู่ซ่อมเรือวิ่งหนีตายกันจ้าละหวั่น เสียงระเบิดยังดังเป็นระยะ ทําให้หน่วยกู้ภัยมูลนิธิสว่างเบญจธรรม และเจ้าหน้าดับเพลิงเทศบาลเมืองสมุทรสงคราม ต้องทยอยออกมาให้พ้นระยะ เบื้องต้น พบศพชายสภาพศพขาดครึ่งท่อน เหลือแต่ท่อนบน และมีผู้ได้รับบาดเจ็บนําส่ง รพ.สมเด็จพระพุทธเลิศหล้า 4 คนโดยมีเสียงระเบิดดังสนั่น 2 ครั้งติดต่อกัน แรงสั่นสะเทือนไปไกลถึง อ.บางคนที ทําให้กระจกบ้านเรือนบริเวณนั้นแตกกระจาย แรงระเบิดส่งให้ปล่องเรือกระเด็นขึ้นฝั่งขาดเป็น 2 ท่อน พนักงานนั่งทํางานหน้าอู่ซ่อมเรือวิ่งหนีตายกันจ้าละหวั่น เสียงระเบิดยังดังเป็นระยะ ทําให้หน่วยกู้ภัยมูลนิธิสว่างเบญจธรรม และเจ้าหน้าดับเพลิงเทศบาลเมืองสมุทรสงคราม ต้องทยอยออกมาให้พ้นระยะ เบื้องต้น พบศพชายสภาพศพขาดครึ่งท่อน เหลือแต่ท่อนบน และมีผู้ได้รับบาดเจ็บนําส่ง รพ.สมเด็จพระพุทธเลิศหล้า 4 คนSPONSOREDนายสมนึก พรหมเขียว ผู้ว่าราชการจังหวัดสมุทรสงคราม กล่าวว่า ช่วงเช้าที่ผ่านมาเรือบรรทุกน้ํามันที่เข้ามาซ่อมได้เกิดระเบิดขึ้น เจ้าหน้าที่กําลังควบคุมเพลิงแต่ค่อนข้างยาก เนื่องจากยังมีน้ํามันตกค้างในเรือ จึงขอสนับสนุนรถดับเพลิงชนิดโฟมจากหลายหน่วยงาน เข้ามาช่วยควบคุม และประสานกรมธุรกิจพลังงานให้ส่งผู้เชี่ยวชาญและเครื่องมือต่างๆ มาช่วย เบื้องต้นในส่วนที่ได้รับผลกระทบมีผู้บาดเจ็บส่งโรงพยาบาลสมเด็จพระพุทธเลิศหล้า 4 ราย ระดับสีเขียวทั้งหมด มีผู้สูญหาย 7 ราย กําลังค้นหาทั้งภายนอก และในเรือ อย่างไรก็ตามได้รับแจ้งจากผู้เชี่ยวชาญว่าอาจจะเกิดระเบิดซ้ําได้ จึงต้องกันพื้นที่ไม่ให้เข้าใกล้บริเวณดังกล่าว และจะไปตั้งศูนย์ช่วยเหลือที่วัดปากสมุทร ตําบลแหลมใหญ่นายสมนึก พรหมเขียว ผู้ว่าราชการจังหวัดสมุทรสงคราม กล่าวว่า ช่วงเช้าที่ผ่านมาเรือบรรทุกน้ํามันที่เข้ามาซ่อมได้เกิดระเบิดขึ้น เจ้าหน้าที่กําลังควบคุมเพลิงแต่ค่อนข้างยาก เนื่องจากยังมีน้ํามันตกค้างในเรือ จึงขอสนับสนุนรถดับเพลิงชนิดโฟมจากหลายหน่วยงาน เข้ามาช่วยควบคุม และประสานกรมธุรกิจพลังงานให้ส่งผู้เชี่ยวชาญและเครื่องมือต่างๆ มาช่วย เบื้องต้นในส่วนที่ได้รับผลกระทบมีผู้บาดเจ็บส่งโรงพยาบาลสมเด็จพระพุทธเลิศหล้า 4 ราย ระดับสีเขียวทั้งหมด มีผู้สูญหาย 7 ราย กําลังค้นหาทั้งภายนอก และในเรือ อย่างไรก็ตามได้รับแจ้งจากผู้เชี่ยวชาญว่าอาจจะเกิดระเบิดซ้ําได้ จึงต้องกันพื้นที่ไม่ให้เข้าใกล้บริเวณดังกล่าว และจะไปตั้งศูนย์ช่วยเหลือที่วัดปากสมุทร ตําบลแหลมใหญ่จากการสอบสวนในเบื้องต้น ทราบว่า เรือบรรทุกน้ํามันดังกล่าวมีน้ํามันเตาอยู่ 25,000 ลิตร และน้ํามันดีเซลค้างอยู่ 20,000 ลิตร ได้มาจอดซ่อมบํารุงภายในท่าเรือแห่งนี้ สันนิษฐานว่าสาเหตุน่าจะเกิดจากการซ่อมหน้าเรือที่มีการอ๊อกเชื่อมเหล็ก แล้วเกิดการปะทุจากการเชื่อมเหล็ก จึงเกิดการระเบิดขึ้น โดยจุดเกิดเหตุมีผู้ปฏิบัติงาน 10 คน มีผู้ปฏิบัติงานบนฝั่ง 30 คนจากการสอบสวนในเบื้องต้น ทราบว่า เรือบรรทุกน้ํามันดังกล่าวมีน้ํามันเตาอยู่ 25,000 ลิตร และน้ํามันดีเซลค้างอยู่ 20,000 ลิตร ได้มาจอดซ่อมบํารุงภายในท่าเรือแห่งนี้ สันนิษฐานว่าสาเหตุน่าจะเกิดจากการซ่อมหน้าเรือที่มีการอ๊อกเชื่อมเหล็ก แล้วเกิดการปะทุจากการเชื่อมเหล็ก จึงเกิดการระเบิดขึ้น โดยจุดเกิดเหตุมีผู้ปฏิบัติงาน 10 คน มีผู้ปฏิบัติงานบนฝั่ง 30 คนส่วนผู้บาดเจ็บ 4 คนคือ นายวินเท นายยาซา นายอาว ชาวพม่า และนายสมพงษ์ ใจวิถี เป็นคนไทย ผู้สูญหาย 7 คน มีนายเชียร หรือลูกพี่เชียร คนไทย ส่วนที่เหลือเป็นชาวพม่า ชื่อนายอาโถ นายโซ นายตี๋ฮะ นายซอมิน นายกูแง และนายทุ่ย เสียชีวิต 1 เป็นชาย ขาขวาขาดกระเด็นไปไกล 500 เมตร นําศพขึ้นที่วัดปากสมุทร ตําบลแหลมใหญ่ ล่าสุดเจ้าหน้าที่พบศพอีก 1 ศพ อยู่ใต้ท้องเรือ  ส่วนผู้บาดเจ็บ 4 คนคือ นายวินเท นายยาซา นายอาว ชาวพม่า และนายสมพงษ์ ใจวิถี เป็นคนไทย ผู้สูญหาย 7 คน มีนายเชียร หรือลูกพี่เชียร คนไทย ส่วนที่เหลือเป็นชาวพม่า ชื่อนายอาโถ นายโซ นายตี๋ฮะ นายซอมิน นายกูแง และนายทุ่ย เสียชีวิต 1 เป็นชาย ขาขวาขาดกระเด็นไปไกล 500 เมตร นําศพขึ้นที่วัดปากสมุทร ตําบลแหลมใหญ่ ล่าสุดเจ้าหน้าที่พบศพอีก 1 ศพ อยู่ใต้ท้องเรือ  สําหรับเรือ smooth sea 22 (สมูทซี 22) กรมเจ้าท่าเเจ้งว่าเรือดังกล่าว เริ่มใบอนุญาตใช้เรือ วันที่ 9 มิถุนายน 2565 และหมดจะอายุใบอนุญาตใช้เรือ วันที่ 30 พฤษภาคม 2566 ระบุประเภทการใช้บรรทุกผลิตภัณฑ์น้ํามัน ประเภทเรือกลเดินทะเลเฉพาะเขตการเดินเรือ ลําน้ําและทะเลระหว่างจังหวัดตราด กับจังหวัดนราธิวาส.สําหรับเรือ smooth sea 22 (สมูทซี 22) กรมเจ้าท่าเเจ้งว่าเรือดังกล่าว เริ่มใบอนุญาตใช้เรือ วันที่ 9 มิถุนายน 2565 และหมดจะอายุใบอนุญาตใช้เรือ วันที่ 30 พฤษภาคม 2566 ระบุประเภทการใช้บรรทุกผลิตภัณฑ์น้ํามัน ประเภทเรือกลเดินทะเลเฉพาะเขตการเดินเรือ ลําน้ําและทะเลระหว่างจังหวัดตราด กับจังหวัดนราธิวาส.SPONSORED ']
        self.Web_thai = Thai(self.data_loadout)
        
    def test_get_location1(self):
        self.assertEqual(self.Web_thai.get_location(), "สมุทรสงคราม")
class location2(unittest.TestCase):
    def setUp(self):
        self.data_loadout2 = ['ณัฐวีร์ นริศชาติ และ นริทร์ ศิริณภัค ร่วมทำงานในวิชา softdev2']
        self.Web_thai2 = Thai(self.data_loadout2)
        
    def test_get_location1(self):
        self.assertEqual(self.Web_thai2.get_location(), "NONE")
class location3(unittest.TestCase):
    def setUp(self):
        self.data_loadout3 = ['อย่าอยู่เลยดีกว่า ชอบจังเลย คลิ๊กเลยที่นี่ ']
        self.Web_thai3 = Thai(self.data_loadout3)
        
    def test_get_location1(self):
        self.assertEqual(self.Web_thai3.get_location(), "เลย")
        
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
        self.sentence_result = unicodedata.normalize("NFKD", self.sentence_result)
        return self.sentence_result
    def get_keyword(self):
        self.keyword_result = {}
        self.keyword_value = self.get_tokenize()
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
    def get_tokenize(self):
        self.word_token = word_tokenize(self.sentence, engine="newmm")
        return self.word_token
    def get_location(self):#convert location dict
        self.location_Result = self.location()
        self.location_counts = {}
        for location, _ in self.location_Result:
            #count location duplicate 
            if location in self.location_counts:
                self.location_counts[location] += 1
            else:
                self.location_counts[location] = 1
                #return max dupicate in location
        try:
            #have location in data
            return max(self.location_counts.keys())
        except:
            #if not have location return none
            return 'NONE'
    def location(self):
        self.data = self.get_tokenize()
        self.location_value = tag_provinces(self.data)
        self.Result_location = filtered_input = [entry for entry in self.location_value if entry[1] == 'B-LOCATION']
        return self.Result_location #Output location Dict
    

if __name__ == '__main__':
    unittest.main()