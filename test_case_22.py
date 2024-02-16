from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_checkout_fail():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    pick_a_product = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link div")
    pick_a_product.click()
    time.sleep(1)
    buy_a_product = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
    )
    buy_a_product_title = driver.find_element(
        By.CSS_SELECTOR, "div.inventory_details_desc_container div"
    )
    buy_a_product_name = buy_a_product_title.text
    buy_a_product.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    shopping_cart.click()
    shopping_cart_product = driver.find_element(
        By.CSS_SELECTOR, "#item_4_title_link div"
    )

    assert buy_a_product_name == shopping_cart_product.text

    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()

    checkout_your_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#header_container div span"))
    )

    firs_tname = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")

    firs_tname.send_keys("")
    last_name.send_keys("")
    postal_code.send_keys("")
    continue_button.click()
    time.sleep(1)
    error_message = driver.find_element(
        By.CSS_SELECTOR, "div.error-message-container.error h3"
    )

    assert error_message.text == "Error: First Name is required"

    driver.quit()
