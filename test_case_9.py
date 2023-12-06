from selenium.webdriver.common.by import By
from utils import login_success, get_driver
import time


driver = get_driver()


def test_browse_products_success():
    login_success(driver)

    product_sort_button = driver.find_element(By.CLASS_NAME, "product_sort_container")
    product_sort_button.click()
    time.sleep(1)
    sort_price_hightolow = driver.find_element(
        By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]'
    )
    sort_price_hightolow.click()

    select_value = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert select_value.get_attribute("value") == "hilo"

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    time.sleep(1)

    the_first_product = driver.find_element(
        By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div'
    )
    the_price_of_the_first_product = float(the_first_product.text.lstrip("$"))
    the_last_product = driver.find_element(
        By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div'
    )
    the_price_of_the_last_product = float(the_last_product.text.lstrip("$"))

    assert the_price_of_the_first_product > the_price_of_the_last_product

    driver.quit()
