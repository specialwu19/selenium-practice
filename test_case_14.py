from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_add_product_into_cart_success():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    buy_a_product_1 = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory"
    )
    buy_a_product_title_1 = driver.find_element(
        By.CSS_SELECTOR, "div.inventory_item div.inventory_item_name"
    )
    buy_a_product_name_1 = buy_a_product_title_1.text
    buy_a_product_1.click()
    time.sleep(1)

    buy_a_product_2 = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
    )
    buy_a_product_title_2 = driver.find_element(
        By.CSS_SELECTOR, "#item_1_title_link div"
    )
    buy_a_product_name_2 = buy_a_product_title_2.text
    buy_a_product_2.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    shopping_cart_nmber_2 = driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container a span"
    )
    shopping_cart_nmber = shopping_cart_nmber_2.text
    shopping_cart.click()

    shopping_cart_product_1 = driver.find_element(
        By.CSS_SELECTOR, "#item_4_title_link div"
    )

    shopping_cart_product_2 = driver.find_element(
        By.CSS_SELECTOR, "#item_1_title_link div"
    )
    assert buy_a_product_name_1 == shopping_cart_product_1.text
    assert buy_a_product_name_2 == shopping_cart_product_2.text
    assert shopping_cart_nmber == "2"


def test_remove_product_success():
    remove_a_product_1 = driver.find_element(
        By.CSS_SELECTOR, "#remove-sauce-labs-backpack"
    )
    remove_a_product_2 = driver.find_element(
        By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt"
    )
    remove_a_product_1.click()
    remove_a_product_2.click()
    time.sleep(1)

    back_to_homepage = driver.find_element(By.CSS_SELECTOR, "#continue-shopping")
    back_to_homepage.click()
    time.sleep(1)
    shopping_cart_nmber_0 = driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container a"
    )

    assert shopping_cart_nmber_0.text == ""

    driver.quit()
