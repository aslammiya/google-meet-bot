from selenium import webdriver
import info
import process
from process import initBrowser
import datetime
from termcolor import colored

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument("--disable-infobars")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("use-fake-device-for-media-stream")
chromeOptions.add_argument("use-fake-ui-for-media-stream")
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chromeOptions)
driver.get('file:///root/programs/g-bot/index.html')

def checkLeav():
    while True:
        ex = driver.find_element_by_class_name('uGOf1d').text
        txt = int(ex)
        if txt == (info.numCheck):
            print('ok')
            try:
                break
                driver.close()
            except Exception:
                print('error')
                break

checkLeav()