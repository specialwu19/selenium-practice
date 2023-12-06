from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_browse_products_success():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

    the_first_product_picture = driver.find_element(
        By.XPATH, '//*[@id="item_4_img_link"]/img'
    )
    the_first_product_title = driver.find_element(
        By.XPATH, '//*[@id="item_4_title_link"]'
    )
    the_first_product_title_name = the_first_product_title.text
    the_first_product_picture.click()
    time.sleep(1)
    the_first_product_own_page_title = driver.find_element(
        By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    )

    assert the_first_product_title_name == the_first_product_own_page_title.text

    driver.quit()
