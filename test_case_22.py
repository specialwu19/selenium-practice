from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_checkout_fail():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

    pick_a_product = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    pick_a_product.click()
    time.sleep(1)
    buy_a_product = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    buy_a_product_title = driver.find_element(
        By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    )
    buy_a_product_name = buy_a_product_title.text
    buy_a_product.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
    shopping_cart.click()
    shopping_cart_product = driver.find_element(
        By.XPATH, '//*[@id="item_4_title_link"]/div'
    )

    assert buy_a_product_name == shopping_cart_product.text

    checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()

    checkout_your_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        )
    )

    firs_tname = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    firs_tname.send_keys("")
    last_name.send_keys("")
    postal_code.send_keys("")
    continue_button.click()
    time.sleep(1)
    error_message = driver.find_element(
        By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3'
    )

    assert error_message.text == "Error: First Name is required"

    driver.quit()
