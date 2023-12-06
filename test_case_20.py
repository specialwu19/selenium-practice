from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time
import re


driver = get_driver()


def test_checkout_success():
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

    firs_tname.send_keys("Janice")
    last_name.send_keys("Wu")
    postal_code.send_keys("412")
    continue_button.click()
    time.sleep(1)

    checkout_product_name = driver.find_element(
        By.XPATH, '//*[@id="item_4_title_link"]/div'
    )
    checkout_product_name = checkout_product_name.text

    checkout_product_price = driver.find_element(
        By.XPATH,
        '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
    )
    checkout_product_price = float(checkout_product_price.text.lstrip("$"))

    item_total_price = driver.find_element(
        By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]'
    )
    item_total_price = item_total_price.text
    price_pattern = r"\$\d+\.\d+"
    match_price = re.search(price_pattern, item_total_price)
    match_price = match_price.group()
    item_total_price = float(str(match_price).lstrip("$"))

    tax_price = driver.find_element(
        By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]'
    )
    tax_price = tax_price.text
    tax_match_price = re.search(price_pattern, tax_price)
    tax_match_price = tax_match_price.group()
    tax_price = float(str(tax_match_price).lstrip("$"))

    total_price = driver.find_element(
        By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]'
    )
    total_price = total_price.text
    total_match_price = re.search(price_pattern, total_price)
    total_match_price = total_match_price.group()
    total_price = float(str(total_match_price).lstrip("$"))

    order_finish = driver.find_element(By.ID, "finish")
    order_finish.click()

    complete = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    assert checkout_product_name == buy_a_product_name
    assert checkout_product_price == item_total_price
    assert item_total_price + tax_price == total_price
    assert complete.text == "Checkout: Complete!"

    driver.quit()
