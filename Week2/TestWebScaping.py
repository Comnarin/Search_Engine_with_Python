from bs4 import BeautifulSoup
import requests
url = "https://football.kapook.com/"
res = requests.get(url)
res.encoding = "utf-8"
if res.status_code == 200:
    print("Successful")
elif res.status_code == 404:
    print("Error 404 page not found")
else:
    print("Not both 200 and 404")
 # soup = BeautifulSoup(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
courses = soup.find_all('a')
# Create an empty list
course_list = []

for course in courses:
    
    # Create a new variable --> obj to store 
    # only course name getting rid of unwanted tags
    obj = course.string
    
    # Append each course into a course_list variable
    course_list.append(obj)
print(course_list)