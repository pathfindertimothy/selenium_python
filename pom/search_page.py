from selenium.webdriver.common.by import By
import time

class SearchPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.my_popup_box = (By.CSS_SELECTOR, '[data-a-target]')
        self.click_search_icon = (By.CSS_SELECTOR, '[aria-label="Search"]')
        self.type_search_word = (By.CSS_SELECTOR, '[type="Search"]')
        self.select_from_list = (By.CSS_SELECTOR, '[title="StarCraft II"]')
        self.click_select_streamer = (By.XPATH, '//*[@role="list"]/div[2]')

    def open_page(self, url):
        self.driver.get(url)

    def close_popup(self):
        self.driver.find_element(*self.my_popup_box).click()

    def search_for_streamer(self):
        self.driver.find_element(*self.click_search_icon).click()
    
    def type_search_string(self, streamer):
        time.sleep(5)
        self.driver.find_element(*self.type_search_word).send_keys(streamer)
    
    def select_item(self):
        time.sleep(5)
        self.driver.find_element(*self.select_from_list).click()

    def scroll_amount(self, num):
        x = 200
        for i in range(num):
            self.driver.execute_script(f'scroll(0, {x})')
            x += 200

    def click_on_streamer(self):
        time.sleep(10)
        self.driver.find_element(*self.click_select_streamer).click()

    def save_item_screenshot(self, choose_location):
        time.sleep(10)
        self.driver.save_screenshot(choose_location)
