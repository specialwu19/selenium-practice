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
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    pick_a_product = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link div")
    pick_a_product.click()
    time.sleep(1)
    buy_a_product = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
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
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.header_secondary_container span")
        )
    )

    firs_tname = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")

    firs_tname.send_keys("Janice")
    last_name.send_keys("Wu")
    postal_code.send_keys("412")
    continue_button.click()
    time.sleep(1)

    checkout_product_name = driver.find_element(
        By.CSS_SELECTOR, "#item_4_title_link div"
    )
    checkout_product_name = checkout_product_name.text

    checkout_product_price = driver.find_element(
        By.CSS_SELECTOR,
        "div.item_pricebar div"
    )
    checkout_product_price = float(checkout_product_price.text.lstrip("$"))

    item_total_price = driver.find_element(
        By.CSS_SELECTOR, "#checkout_summary_container div.summary_subtotal_label"
    )
    item_total_price = item_total_price.text
    price_pattern = r"\$\d+\.\d+"
    match_price = re.search(price_pattern, item_total_price)
    match_price = match_price.group()
    item_total_price = float(str(match_price).lstrip("$"))

    tax_price = driver.find_element(
        By.CSS_SELECTOR, "#checkout_summary_container div.summary_tax_label"
    )
    tax_price = tax_price.text
    tax_match_price = re.search(price_pattern, tax_price)
    tax_match_price = tax_match_price.group()
    tax_price = float(str(tax_match_price).lstrip("$"))

    total_price = driver.find_element(
        By.CSS_SELECTOR, "#checkout_summary_container div.summary_info_label.summary_total_label"
    )
    total_price = total_price.text
    total_match_price = re.search(price_pattern, total_price)
    total_match_price = total_match_price.group()
    total_price = float(str(total_match_price).lstrip("$"))

    order_finish = driver.find_element(By.CSS_SELECTOR, "#finish")
    order_finish.click()

    complete = driver.find_element(By.CSS_SELECTOR, "#header_container div span")

    assert checkout_product_name == buy_a_product_name
    assert checkout_product_price == item_total_price
    assert item_total_price + tax_price == total_price
    assert complete.text == "Checkout: Complete!"

    driver.quit()
