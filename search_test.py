import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pom.search_page as sp

@pytest.fixture()
def driver():
    mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",

    "clientHints": {"platform": "Android", "mobile": True} 
    }

    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=400,890')
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    CHROMEDRIVER_PATH = './drivers/chromedriver.exe'
    service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_open_streamer(driver):
    search_page = sp.SearchPage(driver)
    search_page.open_page("https://m.twitch.tv/")
    search_page.close_popup()
    search_page.search_for_streamer()
    search_page.type_search_string('StarCraft II')
    search_page.select_item()
    search_page.scroll_amount(2)
    search_page.click_on_streamer()
    search_page.save_item_screenshot('./screenshot/streamer_image.png')