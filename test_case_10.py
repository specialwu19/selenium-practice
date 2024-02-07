from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_browse_products_success():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    the_first_product_title = driver.find_element(
        By.CSS_SELECTOR, "div.inventory_item div.inventory_item_name"
    )
    the_first_product_title_name = the_first_product_title.text
    the_first_product_title.click()
    time.sleep(1)

    the_first_product_own_page_title = driver.find_element(
        By.CSS_SELECTOR, "#inventory_item_container div.inventory_details_name.large_size"
    )

    assert the_first_product_title_name == the_first_product_own_page_title.text

    driver.quit()
