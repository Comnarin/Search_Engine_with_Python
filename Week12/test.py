import unittest
import sqlite3
import requests
from bs4 import BeautifulSoup 
from mock import MagicMock
import time
from urllib.parse import urljoin
class spyder:
    def __init__( self ,links,base_url,depth ):
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
            if link.startswith(base_url):
                result.add(link)
        return result
    
    def check_not_domain(self,base_url,links):
        result= set()
        for link in links :
            if not link.startswith(base_url):
                result.add(link)
        return result
    
    def check_ref(self,links,target_links):
        for i in links:
            for j in target_links:
                if i.startswith(j):
                    target_links[j]+=1
        return target_links

class TestSpyder(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://www.example.com"
        self.links = ["https://www.example.com/about", "https://www.example.com/contact"]
        self.depth = 1
        self.spyder = Spyder(self.links, self.base_url, self.depth)
        
    def test_crawl(self):
        visited = self.spyder.crawl(self.base_url, self.depth, 0, set())
        self.assertIn(self.base_url, visited)
        for link in self.links:
            self.assertIn(link, visited)
            
    def test_check_domain(self):
        links = {"https://www.example.com/about", "https://www.example.com/faq", "https://www.google.com"}
        domain_links = self.spyder.check_domain(self.base_url, links)
        self.assertIn("https://www.example.com/about", domain_links)
        self.assertIn("https://www.example.com/faq", domain_links)
        self.assertNotIn("https://www.google.com", domain_links)
        
    def test_check_not_domain(self):
        links = {"https://www.example.com/about", "https://www.example.com/faq", "https://www.google.com"}
        not_domain_links = self.spyder.check_not_domain(self.base_url, links)
        self.assertNotIn("https://www.example.com/about", not_domain_links)
        self.assertNotIn("https://www.example.com/faq", not_domain_links)
        self.assertIn("https://www.google.com", not_domain_links)
        
    def test_check_ref(self):
        links = {"https://www.example.com/about", "https://www.example.com/contact", "https://www.example.com/blog"}
        target_links = {"https://www.example.com/about": 0, "https://www.example.com/contact": 0}
        ref_counts = self.spyder.check_ref(links, target_links)
        self.assertEqual(ref_counts["https://www.example.com/about"], 1)
        self.assertEqual(ref_counts["https://www.example.com/contact"], 1)
        self.assertEqual(ref_counts["https://www.example.com/blog"], 0)


if __name__ == '__main__':
    os.chdir('/Users/narin/Documents/Kmutnb/Year2/S2/Softdev2/Exercise/softdev2/Week12/test.py')
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
