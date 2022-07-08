from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_by_css(driver, css_selector, signal):
    try:
        WebDriverWait(driver, 20).until(           
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        return True
    except:
        print("wait failed: " + signal)
        return False
    
def turnToFinalWindow(driver):
    driver.switch_to.window(driver.window_handles[-1])