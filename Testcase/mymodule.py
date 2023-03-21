# %%
import requests
from bs4 import BeautifulSoup 
import re
import unicodedata
import pythainlp.util
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
#from pythainlp.summarize import extract_keywords
from pythainlp.summarize import summarize
import itertools
from urllib.parse import urljoin
import time
from pythainlp.tag import tag_provinces
from pythainlp.tokenize import word_tokenize as tokenizer
from datetime import datetime
import math


# %%
class spyder:
    def __init__( self ,links,base_url,depth ):
        if not base_url.startswith('http://') and not base_url.startswith('https://'):
            base_url = 'http://' + base_url
        self.base_url = base_url
        target_links={}
        for i in links:
            target_links[i]=0 
        self.target_links = target_links
        self.depth = depth
    
    def get_crawler(self):
        self.result_crawler = self.crawl(self.base_url,self.depth,0,set())
        return self.result_crawler
    
    def get_check_domain(self):
        print("get_check_domain called")
        print("target_links:", self.target_links)
        self.check_domain_result = self.check_domain(self.base_url,self.get_crawler())
        return self.check_domain_result
    
    def get_check_not_domain(self):
        self.check_not_domain_result = self.check_not_domain(self.base_url,self.get_crawler())   
        return self.check_not_domain_result
    
    def get_check_ref(self):
        self.check_ref_result = self.check_ref(self.get_check_not_domain(),self.target_links)
        return self.check_ref_result
    
    def crawl(self,url,n, depth,visited):
        if depth < n :
            visited.add(url)
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
            time.sleep(0.3)
            response = requests.get(url,headers=headers)
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
            except:
                soup = BeautifulSoup(response.text, 'lxml')
            links = soup.find_all('a')
            links = [link.get('href') for link in links if link.get('href') and not link.get('href').startswith('#')]
            links = [urljoin(url, link) for link in links if link]

            for link in links:
                if link not in visited:
                    link = link.replace(' ','')
                    visited.add(link)
                    if link.startswith(url):
                        self.crawl(link,n=n,depth=depth+1, visited=visited)
        return visited
    
    def check_domain(self,base_url,links):
        result= set()
        for link in links :
            if link.startswith("https"):
                link = "http" + link[5:]
                if link.startswith(base_url):
                    result.add(link)
            else:
                if link.startswith(base_url):
                    result.add(link)
        return result
    
    def check_not_domain(self,base_url,links):
        result= set()
        for link in links :
            if link.startswith("https"):
                link = "http" + link[5:]
                if not link.startswith(base_url):
                    result.add(link)
            else:
                if not link.startswith(base_url):
                    result.add(link)
        return result
    
    def check_ref(self,links,target_links):
        for i in links:
            for j in target_links:
                if i.startswith(j):
                    target_links[j]+=1
        return target_links

# %%
import sqlite3
def create_db(self):
    conn = sqlite3.connect('inverted_index.db')

    # Create tables for words, documents, and word frequencies

    conn.execute('''
    CREATE TABLE words (
        ID INTEGER PRIMARY KEY,
        Word TEXT NOT NULL UNIQUE
    );
    ''')

    conn.execute('''
    CREATE TABLE documents (
        ID INTEGER PRIMARY KEY,
        Link TEXT NOT NULL UNIQUE ,
        Title TEXT,
        Body TEXT,
        Location TEXT,
        Ref INT,
        Time TEXT
    );
    ''')

    conn.execute('''
    CREATE TABLE word_frequencies (
        Word_ID INTEGER ,
        Doc_ID INTEGER ,
        Frequency INTEGER NOT NULL,
        TF_IDF REAL ,
        PRIMARY KEY (word_id, doc_id),
        FOREIGN KEY (word_id) REFERENCES words(id),
        FOREIGN KEY (doc_id) REFERENCES documents(id)
    );
    ''')
    conn.execute('''
    CREATE TABLE Temp_link(
        ID INTEGER PRIMARY KEY,
        Link TEXT NOT NULL UNIQUE
    );
    ''')

    conn.execute('''
    CREATE TABLE Domain_link(
        ID INTEGER PRIMARY KEY,
        Domain_Link TEXT NOT NULL UNIQUE
    );
    ''')
    conn.commit()

# %%
def Crawl_to_temp(target_links,db):
    print("Crawl_to_temp function called")
    print("target_links:", target_links)
    conn = sqlite3.connect(db)
    for i in target_links:
        domain = conn.execute("SELECT id FROM domain_link  WHERE domain_link  = ?", (i,)).fetchone()
        if not domain:
            conn.execute("INSERT INTO domain_link (domain_link) VALUES (?)", (i,))
            conn.commit()
        web_spyder = spyder(target_links,i,2)
        domainlinks  = web_spyder.get_check_domain()
        for link in domainlinks:
            conn.execute('''INSERT INTO Temp_link (Link) VALUES (?);''', (link,))
            conn.commit()

# %%
# target_links = ['http://www.bbc.com/news','http://www.thairath.co.th']
# Crawl_to_temp(target_links,'inverted_index.db')

# %%
class Thai:
    def __init__(self,data:list):
        self.data_value = data
        self.sentence = self.get_sentence()
        self.summarize = self.get_summarize()
        self.word = self.get_word() 
    def make_sentence(self,list_word):
        list_word = [list_word]
        self.sentence_value = ''
        for i in list_word:
            for i in list_word:
                if pythainlp.util.countthai(i)<10:
                    list_word.remove(i)
        self.sentence_value = ' '.join(list_word)
        return self.sentence_value
    def get_sentence(self):
        self.sentence_result = self.make_sentence(self.data_value)
        return self.sentence_result
    def get_word(self):
        self.word_value = tokenizer(self.sentence, engine="newmm")
        return self.word_value
    def get_summarize(self):
        self.summarize_result =[]
        self.summarize_result = summarize(self.sentence,n=5)
        return self.summarize_result
    def location(self):
        self.data = self.get_word()
        self.location_value = tag_provinces(self.data)
        self.Result_location = [entry for entry in self.location_value if entry[1] == 'B-LOCATION']
        return self.Result_location

# %%
def spacy_process(text):
    filtered_sentence =[]
    nlp = spacy.load('en_core_web_sm') 
    try:
        doc = nlp(text)
        lemma_list = []
        for token in doc:
            lemma_list.append(token.lemma_)
        
        for word in lemma_list:
            lexeme = nlp.vocab[word]
            if lexeme.is_stop == False:
                filtered_sentence.append(word)    
        punctuations="?:!.,;"
        for word in filtered_sentence:
            if word in punctuations:
                filtered_sentence.remove(word)
        return filtered_sentence
    except:
        return ['No word found']
        
 
    
    

# %%
def cleansing(body):
    for i in body:
        output = i.replace('\n', '  ').replace('\xa0', '  ').replace('®', ' ').replace(';', ' ').replace('â', ' ')
        output = " ".join(output.split())
    return output

# %%
def scrap_tags(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title').text
        if title_tag == '404 - Not Found':
            title_tag ='Not Found Title'
    except:
        try:
            title_tag = soup.find('title')
        except:
            title_tag = 'Not Found Title'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        body_tag = soup.find('body')
        text_below_body = body_tag.get_text().lower()
    except:
        text_below_body = title_tag
        if text_below_body =='Not Found Title':
            text_below_body = 'Not Found Body'
    body_list =[]
    body_list.append(text_below_body)
    return (body_list,title_tag)

# %%
def get_word(body):
    word_freq = {}
    for word in body:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

# %%
#เอาเพิ่ม
def get_ref():
    conn = sqlite3.connect('inverted_index.db')
    domain = conn.execute("SELECT domain_link FROM domain_link ;").fetchall()
    domain = [t[0] for t in domain]
    for i in domain :
        web = spyder(domain,i,2)
        ref = web.get_check_ref()
    return ref

# %%
#เอาเพิ่ม
def update_ref():
    conn = sqlite3.connect('../Week10/inverted_index2.db')
    domain = conn.execute("SELECT domain_link FROM domain_link ;").fetchall()
    domain = [t[0] for t in domain]
    for i in domain :
        web = spyder(domain,i,1)
        ref = web.get_check_ref()
    check_link = conn.execute("SELECT link FROM documents ;").fetchall()
    check_link = [t[0] for t in check_link]
    for j in check_link:
        for k in ref:
            if j.startswith(k):
                conn.execute('UPDATE documents SET REF = ? WHERE link = ? ', (ref[k], j,))
    conn.commit()

# %%
#เอาเพิ่ม
import locationtagger
def eng_location(data,title):
    entities = locationtagger.find_locations(text = data[0])
    location = entities.countries
    if location == []:
        entities = locationtagger.find_locations(text = title)
        location = entities.countries
        if location ==[]:
            location = ['None']
    return location        

# %%
#เอาเพิ่ม
def check_lang(url:str):
    data_lang,title = scrap_tags(url)
    try:
        percent = pythainlp.util.countthai(data_lang[0][0])
        if percent >50:
            thai_nlp = Thai(data_lang[0]) 
            word = thai_nlp.word
            try:
                location = 'จ.'+max(thai_nlp.get_location().keys())
            except:
                location = 'Thailand'
            new_list = [s.strip().replace('"', '') for s in word if s.strip()]
            while '' in new_list:
                new_list.remove('')
            word = get_word(new_list)
            return data_lang,word,title,location
        else:
            clean_body=cleansing(data_lang)
            body = spacy_process(cleansing(data_lang))
            word = get_word(body)
            location = eng_location(data_lang,title)
            return clean_body,word,title,location
    except:
        clean_body=cleansing(data_lang)
        body = spacy_process(cleansing(data_lang))
        word = get_word(body)
        location = eng_location(data_lang,title)
        return clean_body,word,title,location

# %%
#เอาเพิ่ม
def make_doc(link,ref):
    link.replace(" ", "")
    d=dict()    
    body,word,title,location =check_lang(link)
    d['link']= link
    d['title'] = title
    d['body']=body
    d['location']=location
    d['word'] = word
    for i in ref:
        if link.startswith(i):
            d['ref'] = ref[i] 
    print(d)
    return d

# %%
def update_tf_idf():
    conn = sqlite3.connect('inverted_index.db',timeout=3)

    cursor = conn.execute('SELECT COUNT(*) FROM documents')
    N = cursor.fetchone()[0]
    
    cursor = conn.execute('SELECT ID, Word FROM words')
    words = cursor.fetchall()
    
    for word in words:
        word_id = word[0]
        word_str = word[1]

        cursor = conn.execute('SELECT Doc_ID, Frequency FROM word_frequencies WHERE Word_ID = ?', (word_id,))
        doc_freqs = cursor.fetchall()

        df = len(doc_freqs)
        idf = math.log(N / df)

        for doc_freq in doc_freqs:
            doc_id = doc_freq[0]
            tf = doc_freq[1]
            tf_idf = tf * idf
            conn.execute('UPDATE word_frequencies SET TF_IDF = ? WHERE Word_ID = ? AND Doc_ID = ?', (tf_idf, word_id, doc_id))

    conn.commit()

# %%
def insert_to_database(doc):
  conn = sqlite3.connect('../week11/inverted_index.db')
  for i in doc:
    conn.execute('''INSERT INTO documents (Link, Title, Body, Location, Ref, Time) VALUES (?, ?, ?, ?, ?, ?);''', (str(i['link']), str(i['title']), str(i['body']), str(i['location']), int(i['ref']), datetime.now()))
    doc_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    
    for j in i['word'].keys():
      word_id = conn.execute("SELECT id FROM words WHERE word = ?", (j,)).fetchone()
      if not word_id:
        conn.execute("INSERT INTO words (word) VALUES (?)", (j,))
        word_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
      else:
        word_id = word_id[0]
      
      conn.execute('''INSERT INTO word_frequencies (word_id, doc_id, Frequency) VALUES (?, ?, ?);''', (word_id, doc_id, i['word'][j]))
  
 
  conn.commit()
  # update_tf_idf()

# %%
#เอาเพิ่ม
def temp_to_index(conn):
    #conn = sqlite3.connect('inverted_index.db')
    links = conn.execute('SELECT Link FROM temp_link ').fetchall()
    links = [t[0] for t in links]
    ref=get_ref()
    for i in links:
        doc = make_doc(i,ref)
        insert_to_database([doc])
        conn.execute('DELETE FROM temp_link WHERE link = ?; ', (i,))
        conn.commit()


# %%
import ast

def location_search():
    conn = sqlite3.connect('../week11/inverted_index.db')
    cursor = conn.cursor()

    # Split the query into individual words
    search_term = [str(input())]
    clean_sentence = cleansing(search_term)
    words = spacy_process(clean_sentence)

    # Retrieve the documents that contain each word
    doc_lists = []
    for word in words:
        cursor.execute("SELECT Doc_ID, TF_IDF FROM word_frequencies JOIN words ON words.ID = word_frequencies.word_ID WHERE word = ?", (word,))
        doc_list = cursor.fetchall()
        doc_lists.append(doc_list)

    # Merge the document lists using the TF-IDF scores
    doc_scores = {}
    for doc_list in doc_lists:
        for doc_id, tf_idf in doc_list:
            if doc_id in doc_scores:
                doc_scores[doc_id] += tf_idf
            else:
                doc_scores[doc_id] = tf_idf

    # Rank the documents by their overall relevance
    ranked_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)

    # Retrieve the links and titles of the top documents
    results = []
    for doc_id, score in ranked_docs:
        cursor.execute("SELECT location FROM documents WHERE ID = ?", (doc_id,))
        location = cursor.fetchone()
        location = location[0].strip("()[]'").replace("'", "").split(", ")
        title = cursor.execute("SELECT title FROM documents WHERE ID = ?", (doc_id,)).fetchone()[0]
        results.append((location, title))

    conn.close()
    


    return results

# %%
from geopy.geocoders import Nominatim
def get_lat_lon(data):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(data)
        latitude,longtitude = location.latitude, location.longitude
    except:
        latitude,longtitude = 'Not found','Not found'
    return (latitude,longtitude)

# %%
data = location_search()
print(data)
result =[]
for i in data:
    coordinate = []
    for j in i[0]:
        lat,lon =  get_lat_lon(j)
        coordinate.append([lat,lon])
    result .append((coordinate,i[1]))
    
print(result)
# %%
def group(results):


    # Group the results by location
    grouped_results = {}
    for coords, title in results:
        for country in coords:
            if country in grouped_results:
                grouped_results[country].append(title)
            else:
                grouped_results[country] = [title]

    # Compute the count of titles for each location
    count_of_titles = {}
    for coords, titles in grouped_results.items():
        count_of_titles[coords] = len(titles)

    # Combine the location, titles, and title count into a single output
    output_list = []
    for coords, titles in grouped_results.items():
        output_list.append((coords, titles, count_of_titles[coords]))

    return output_list
        
# %%
def sentence_search():
    conn = sqlite3.connect('../week12/inverted_index.db')
    cursor = conn.cursor()

    # Split the query into individual words
    search_term = [str(input())]
    clean_sentence = cleansing(search_term)
    words = spacy_process(clean_sentence)

    # Retrieve the documents that contain each word
    doc_lists = []
    for word in words:
        cursor.execute("SELECT Doc_ID, TF_IDF FROM word_frequencies JOIN words ON words.ID = word_frequencies.word_ID WHERE word = ?", (word,))
        doc_list = cursor.fetchall()
        doc_lists.append(doc_list)

    # Merge the document lists using the TF-IDF scores
    doc_scores = {}
    for doc_list in doc_lists:
        for doc_id, tf_idf in doc_list:
            if doc_id in doc_scores:
                doc_scores[doc_id] += tf_idf
            else:
                doc_scores[doc_id] = tf_idf

    # Rank the documents by their overall relevance
    ranked_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
    print(ranked_docs)

    # Retrieve the locations and titles of the top documents
    results = []
    for doc_id, score in ranked_docs:
            cursor.execute("SELECT Link, Title FROM documents WHERE ID = ?", (doc_id,))
            link, title = cursor.fetchone()
            results.append((link, title))

    conn.close()

    return results
# %%
