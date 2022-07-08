from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import common
import selenium_base

class MyDriver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.headless = True
        self.driver = webdriver.Chrome(options=options,
                                       executable_path="./chromedriver.exe")
    def begin(self):
        # time.sleep(5)
        self.driver.get("https://opensea.io/rankings")
        for i in range(1, 11):
            self.to_next_page()
        for i in range(1, 11):
            self.process_single_page()
            self.to_next_page()
    
    def process_single_page(self):
        selenium_base.wait_by_css(self.driver, "[role='listitem']", "ranking_page")
        print("hello wait")
        href_set = set()
        raw_list = []
        old_scroll_top = 0
        while True:
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
            time.sleep(1)
            new_scoll_top = self.driver.execute_script("return document.documentElement.scrollTop")
            if new_scoll_top == old_scroll_top:
                break
            old_scroll_top = new_scoll_top

            collection_a = self.driver.find_elements_by_css_selector("[role='listitem']")
            raw_list.extend(collection_a)
            for list_item in collection_a:
                href_set.add(list_item.find_element_by_tag_name("a").get_attribute("href"))
        
        print(len(href_set))
        common.output("../data/collection_hrefs_part2.txt", href_set)
        # for href in href_set:
        #     print(href)
    
    def to_next_page(self):
        # next_page_btn = self.driver.find_element_by_id("main")\
        #                            .find_elements_by_tag("div")[2]\
        #                            .find_elements_by_tag("button")[1]
        next_page_btn = self.driver.find_element_by_css_selector("[value='arrow_forward_ios']")
        next_page_btn.click()
        time.sleep(5)
        
if __name__ == '__main__':
    print("hello")
    driver = MyDriver()
    driver.begin()
    