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
    sort_price_hightolow = driver.find_element(
        By.CSS_SELECTOR,
        "div.header_secondary_container select.product_sort_container option[value='hilo']",
    )
    sort_price_hightolow.click()

    select_value = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")

    assert select_value.get_attribute("value") == "hilo"

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    time.sleep(1)

    item_prices = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item_price")
    the_first_product_price = float(item_prices[0].text.lstrip("$"))
    the_last_product_price = float(item_prices[-1].text.lstrip("$"))

    assert the_first_product_price > the_last_product_price

    driver.quit()
