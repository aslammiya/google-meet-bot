from selenium import webdriver
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time; import getpass; import datetime; import threading; import os
from twilio.rest import Client
import datefinder
import datetime
from termcolor import colored
import re; import requests
import info

USERNAME = "aslammiya722@gmail.com"
PASSWORD = "123@Aslam"

usernameFieldPath = "identifierId"
usernameNextButtonPath = "identifierNext"
passwordFieldPath = "password"
passwordNextButtonPath = "passwordNext"
micBlockPath = "//div[@aria-label='Turn off microphone (ctrl + d)']"
cameraBlockPath = "//div[@aria-label='Turn off camera (ctrl + e)']"
joinButton1Path = "//span[contains(text(), 'Join')]"
statusPath = "//div[@role='status']"
joinButton2Path = "//span[contains(text(), 'Ask to join')]"
listButtonPath = "//button[@aria-label='Chat with everyone']"
listButtonCrossPath = "//button[@aria-label='Close']"
studentNumberPath = "//div[@class='uGOf1d']"
endButtonPath = "[aria-label='Leave call']"

def initBrowser():
    print(colored('\n    Browser initialising....', 'cyan'))
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("use-fake-device-for-media-stream")
    chromeOptions.add_argument("use-fake-ui-for-media-stream")
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver
    driver = webdriver.Chrome(options=chromeOptions)
    print(colored("    Success!", 'green'))
    return(driver)

def login():
    print(colored('\n    logining to Google account....', 'cyan'))
    driver.get('https://accounts.google.com/signin')
    wait = WebDriverWait(driver, 5)
    usernameField = wait.until(when.element_to_be_clickable((by.ID, usernameFieldPath)))
    time.sleep(1)
    usernameField.send_keys(USERNAME)

    usernameNextButton = wait.until(when.element_to_be_clickable((by.ID, usernameNextButtonPath)))
    usernameNextButton.click()

    passwordField = wait.until(when.element_to_be_clickable((by.NAME, passwordFieldPath)))
    time.sleep(2)
    passwordField.send_keys(PASSWORD)

    passwordNextButton = wait.until(when.element_to_be_clickable((by.ID, passwordNextButtonPath)))
    passwordNextButton.click()

    time.sleep(3)
    print(colored("    Success!", 'green'))
    time.sleep(1)

def attendMeet(link):
    global STATUS, BROWSER_DRIVER
    print(colored("\n    Navigating to Google Meet... ", 'cyan'))
    print(colored("    Success!", 'green'))
    print(colored("\n    Entering Google Meet... ", 'cyan'))
    driver.get(link)

    while True:
        try:
            joinButton = WebDriverWait(driver, 2).until(when.element_to_be_clickable((by.XPATH, joinButton1Path)))
            status = driver.find_element_by_xpath(statusPath).get_attribute('textContent')
            if status == "No one else is here":
                print(colored("\n    No one is in the meeting, sleeping for 5 minutes for the last time then skipping", 'red'))
                time.sleep(5)
                clrscr()
                print(MENU, end="")
                time.sleep(300)
                status = driver.find_element_by_xpath(statusPath).get_attribute('textContent')
                if status == "No one else is here":
                    clrscr()
                    print(colored("\n    Omiting the current meeting because of timout error", 'red'))
                    time.sleep(5)
                    return 0
            break
        except Exception:
            pass

        try:
            joinButton = WebDriverWait(driver, 2).until(when.element_to_be_clickable((by.XPATH, joinButton2Path)))
            break
        except Exception:
            pass
    permision = True
    if permision == True:
        micBlockButton = driver.find_element_by_xpath(micBlockPath)
        cameraBlockButton = driver.find_element_by_xpath(cameraBlockPath)
        time.sleep(0.5)
        cameraBlockButton.click()
        time.sleep(0.5)
        micBlockButton.click()

    time.sleep(1)
    while True:
        try:
            joinButton.click()
            break
        except Exception:
            time.sleep(2)

    print(colored("    Success!", 'green'))
    time.sleep(1)

    while True:
        try:
            listButton = driver.find_element_by_xpath(listButtonPath)
            listButton.click()
            break
        except Exception:
            try:
                joinButton = driver.find_element_by_xpath(joinButton1Path)
                time.sleep(1)
                joinButton.click()
            except Exception: 
                pass
            time.sleep(1)

    joinSms()
    print(colored("\n    Now attending Google Meet", 'green'))
    STATUS = "Attending meeting"
    time.sleep(2)
    print(end="")
    return 1

def endMeet():
    try:
        listCrossButton = driver.find_element_by_xpath(listButtonCrossPath)
        listCrossButton.click()
    except Exception:
        listButton = driver.find_element_by_xpath(listButtonPath)
        listButton.click()
    time.sleep(1)
    endButton = driver.find_element_by_css_selector(endButtonPath)
    endButton.click()
    leavedSms()
    print(colored("\n    Successfully ended Google Meet", 'green'))
    time.sleep(2)
    print(end="")

def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def quit():
    time.sleep(3)
    driver.quit()

def wait():
	time.sleep(info.waitTime)

def botRimender(time):
    timeExt = datefinder.find_dates(time)
    for i in timeExt:
        pass
    strA = str(i)
    time = strA[11:]
    hor = time[:-6]
    hor = int(hor)
    minA = time[3:-3]
    minA = int(minA)
    print(colored(f'\n    Start joining lecture at {hor}:{minA} ...', 'green'))

    while True:
        if hor == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                break

def joinSms():
    client = Client('ACca4370fa84a441110e01815fded97904','7e73844feeabaf0366a520ac36a1b6a5')
    client.messages.create(from_=18649027504, body=info.joinMessage, to=919820654116)

def leavedSms():
    client = Client('ACca4370fa84a441110e01815fded97904','7e73844feeabaf0366a520ac36a1b6a5')
    client.messages.create(from_=18649027504, body=info.leaveMessage, to=919820654116)

def errorSms():
    client = Client('ACca4370fa84a441110e01815fded97904','7e73844feeabaf0366a520ac36a1b6a5')
    client.messages.create(from_=18649027504, body=info.errSms, to=919820654116)

def checkLeav():
    while True:
        try:
            ex = driver.find_element_by_class_name('uGOf1d').text
            txt = int(ex)
            if txt == (info.numCheck):
                endMeet()
                driver.close()
        except Exception:
            pass
            break

