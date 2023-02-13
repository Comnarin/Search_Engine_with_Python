from selenium import webdriver
import undetected_chromedriver as uc
import time
t = time.localtime()

browser = uc.Chrome()
browser.get("https://docs.google.com/forms/d/e/1FAIpQLScA1SJqTZ_hMccIZQkalVsfJZWcWXMpH_eLNcyeqEWrKpEUqA/viewform?usp=sf_link")
username = "email"
password = "passsword"

time.sleep(1)
login = browser.find_element("xpath", '/html/body/div[2]/div/div[2]/div[3]/div[2]')
login.click()

time.sleep(1)
username_input = browser.find_element("xpath", '//*[@id="identifierId"]')
username_nextbutton = browser.find_element("xpath", '//*[@id="identifierNext"]/div/button')
username_input.send_keys(username)
username_nextbutton.click()
time.sleep(5)

password_input = browser.find_element("xpath", '//*[@id="password"]/div[1]/div/div[1]/input')
password_nextbutton = browser.find_element("xpath", '//*[@id="passwordNext"]/div/button')
password_input.send_keys(password)
password_nextbutton.click()
time.sleep(10)

# Use the following snippets to get elements by their class names
name = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_input = name.send_keys("Narin")
sirname = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
sirname = sirname.send_keys("Sirinapuk")

age = browser.find_element("xpath", '//*[@id="i26"]/div[3]/div')
age_input = age.click()

rating = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
rating_input = rating.click()

thai_food = browser.find_element("xpath", '//*[@id="i47"]/div[2]')
thai_food.click()

date = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date.send_keys('26/09/2001')

current_time = time.strftime("%H:%M", t)
hours,minute = current_time.split(':')
hour_input = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
hour_input.send_keys(hours)
minute_input = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
minute_input.send_keys(minute)

choose = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
choose_click =choose.click()
time.sleep(1)
male = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[3]/span')
#browser.execute_script("arguments[0].click();", male)
#male = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[1]/div[3]/span')
browser.execute_script("arguments[0].click();", male)
#male.click()
time.sleep(5)
submitbutton = browser.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submitbutton.click()
time.sleep(5)
browser.close()
