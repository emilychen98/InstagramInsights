from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import json

def findHashtag(json_tags):
    delay = 5
    options = Options()
    options.headless = True
    # profile = FirefoxProfile("/home/emily/.mozilla/firefox/ujbj6kw3.test")    
    profile = FirefoxProfile("C:/Users/XingLu Wang/AppData/Roaming/Mozilla/Firefox/Profiles/is2dwfxg.tester")

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

    if browser.find_elements_by_css_selector("button.sqdOP:nth-child(4)"):
        save_info_button = browser.find_element_by_css_selector("button.sqdOP:nth-child(4)")
        save_info_button.click()

    if browser.find_elements_by_css_selector("button.aOOlW:nth-child(2)"):
        not_now_button = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        not_now_button.click()
    
    data = json.loads(json_tags)
    hashtags = data["hashtags"]

    ig_dict = dict()
    hashtag_counts_dict  = dict()

    for hashtag in hashtags:  
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]'))
        WebDriverWait(browser, delay).until(element_present)        
        browser.get('https://www.instagram.com/explore/tags/' + hashtag[1:len(hashtag)])
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/header/div[2]/div/div[2]/span/span'))
        WebDriverWait(browser, delay).until(element_present)        
        post_count = browser.find_element_by_xpath('/html/body/div[1]/section/main/header/div[2]/div/div[2]/span/span').text
        hashtag_counts_dict[hashtag] = post_count

    ig_dict["hashtags"] = hashtag_counts_dict
    browser.close()

    # return a JSON string
    return json.dumps(ig_dict)
