from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile

options = Options()
options.headless = True

hashtag = "#vancouver"

profile = FirefoxProfile("/home/emily/.mozilla/firefox/ujbj6kw3.test")
browser = webdriver.Firefox(firefox_profile=profile, options=options)

browser.implicitly_wait(2)
browser.get('https://www.instagram.com/')

if browser.find_elements_by_xpath("//a[text()='Log in']"):
    login_link = browser.find_element_by_xpath("//a[text()='Log in']")
    login_link.click()
    sleep(1)

if browser.find_elements_by_css_selector("input[name='username']"):
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys("instaInsightsTest")
    password_input.send_keys("instaInsights123")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

print("debug 1")

if browser.find_elements_by_css_selector("button.sqdOP:nth-child(4)"):
    save_info_button = browser.find_element_by_css_selector("button.sqdOP:nth-child(4)")
    save_info_button.click()

print("debug 2")


if browser.find_elements_by_css_selector("button.aOOlW:nth-child(2)"):
    not_now_button = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    not_now_button.click()

print("debug 3")

search_value = browser.find_element_by_css_selector("input[placeholder='Search']")
search_value.send_keys(hashtag)
sleep(0.5)
search_value.send_keys(Keys.ARROW_DOWN)
search_value.send_keys(Keys.RETURN)

print("debug 4")


post_count = 0
for elem in browser.find_elements_by_xpath('/html/body/div[1]/section/main/header/div[2]/div/div[2]/span/span'):
    post_count = elem.text

print("Hashtag: ", hashtag, " Count: ", post_count)
browser.close()
