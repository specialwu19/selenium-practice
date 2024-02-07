from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_add_product_into_cart_and_remove_success():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    buy_a_product = driver.find_element(By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
    buy_a_product_title = driver.find_element(
        By.CSS_SELECTOR, "div.inventory_item div.inventory_item_name"
    )
    buy_a_product_name = buy_a_product_title.text
    buy_a_product.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    shopping_cart_nmber_1 = driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container a.shopping_cart_link span"
    )
    shopping_cart_nmber = shopping_cart_nmber_1.text
    shopping_cart.click()
    shopping_cart_product = driver.find_element(
        By.CSS_SELECTOR, "div.cart_item div.inventory_item_name"
    )

    assert buy_a_product_name == shopping_cart_product.text
    assert shopping_cart_nmber == "1"

    remove_a_product = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn_secondary.btn_small.cart_button"
    )
    remove_a_product.click()
    time.sleep(1)
    back_to_homepage = driver.find_element(By.CSS_SELECTOR, "#continue-shopping")
    back_to_homepage.click()
    time.sleep(1)
    shopping_cart_nmber_0 = driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container a"
    )

    assert shopping_cart_nmber_0.text == ""

    driver.quit()
