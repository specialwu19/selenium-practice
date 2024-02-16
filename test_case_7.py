from selenium.webdriver.common.by import By
from utils import login_success, get_driver
import time


driver = get_driver()


def test_browse_products_success():
    login_success(driver)

    product_sort_button = driver.find_element(
        By.CSS_SELECTOR, ".product_sort_container"
    )
    product_sort_button.click()
    time.sleep(1)
    sort_ztoa = driver.find_element(
        By.CSS_SELECTOR,
        "div.header_secondary_container select.product_sort_container option[value='za']",
    )
    sort_ztoa.click()

    select_value = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")

    assert select_value.get_attribute("value") == "za"

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    time.sleep(1)

    the_first_product = driver.find_element(By.CSS_SELECTOR, "#item_3_title_link div")
    the_first_letter_of_the_first_product = str(the_first_product.text[0])
    the_last_product = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link div")
    the_first_letter_of_the_last_product = str(the_last_product.text[0])

    assert the_first_letter_of_the_first_product > the_first_letter_of_the_last_product

    driver.quit()
