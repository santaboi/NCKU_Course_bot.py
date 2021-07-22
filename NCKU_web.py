from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from PIL import Image
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
url = "https://course.ncku.edu.tw/" 
browser.get(url) 

log_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fas.fa-sign-in-alt")))
log_button.click()

try :
    print("inputing username and password...") 
    user_id = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "user_id")))
    user_id.send_keys("") #personal_ID : fill in yourself!!!!!!!!!!!!!
    password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "passwd")))
    password_input.send_keys("") #personal_password : fill in yourself!!!!!!!!!!!!!!!!

    #verification code  (若CNN judge 失敗 要跑loop)
    browser.save_screenshot("image.png")
    v_code = browser.find_element_by_class_name('click')
    # v_code location     
    print(v_code.location)
    print(v_code.size)
    left = v_code.location['x']
    right = v_code.location['x'] + v_code.size['width']
    top = v_code.location['y']
    bottom = v_code.location['y'] + v_code.size['height']
    v_img = Image.open("image.png")
    v_img = v_img.crop((left , top , right , bottom))
    v_img.show()
except :
    browser.quit()
