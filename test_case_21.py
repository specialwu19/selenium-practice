from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver, get_price
import time


driver = get_driver()


def test_checkout_success():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    pick_a_product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link div")
    pick_a_product_1.click()
    time.sleep(1)
    buy_a_product_1 = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
    )
    buy_a_product_title_1 = driver.find_element(
        By.CSS_SELECTOR,
        "#inventory_item_container div.inventory_details_name.large_size",
    )
    buy_a_product_name_1 = buy_a_product_title_1.text
    buy_a_product_1.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    shopping_cart.click()
    shopping_cart_product_1 = driver.find_element(
        By.CSS_SELECTOR, "#item_4_title_link div"
    )

    assert buy_a_product_name_1 == shopping_cart_product_1.text

    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()

    checkout_your_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#header_container div span"))
    )

    first_tname = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")

    first_tname.send_keys("Janice")
    last_name.send_keys("Wu")
    postal_code.send_keys("412")
    continue_button.click()
    time.sleep(1)

    cancel_button = driver.find_element(By.CSS_SELECTOR, "#cancel")
    cancel_button.click()

    pick_a_product_2 = driver.find_element(By.CSS_SELECTOR, "#item_5_title_link div")
    pick_a_product_2.click()
    time.sleep(1)
    buy_a_product_2 = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket"
    )
    buy_a_product_title_2 = driver.find_element(
        By.CSS_SELECTOR,
        "#inventory_item_container div.inventory_details_name.large_size",
    )
    buy_a_product_name_2 = buy_a_product_title_2.text
    buy_a_product_2.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    shopping_cart.click()
    shopping_cart_product_2 = driver.find_element(
        By.CSS_SELECTOR, "#item_5_title_link div"
    )

    assert buy_a_product_name_2 == shopping_cart_product_2.text

    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()

    checkout_your_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#header_container div span"))
    )

    first_tname = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")

    first_tname.send_keys("Janice")
    last_name.send_keys("Wu")
    postal_code.send_keys("412")
    continue_button.click()
    time.sleep(1)

    checkout_product_name_1 = driver.find_element(
        By.CSS_SELECTOR, "#item_4_title_link div"
    )
    checkout_product_name_2 = driver.find_element(
        By.CSS_SELECTOR, "#item_5_title_link div"
    )
    checkout_product_name_1 = checkout_product_name_1.text
    checkout_product_name_2 = checkout_product_name_2.text

    checkout_product_prices = driver.find_elements(
        By.CSS_SELECTOR, ".inventory_item_price"
    )

    assert len(checkout_product_prices) == 2

    checkout_product_price_1 = float(checkout_product_prices[0].text.lstrip("$"))
    checkout_product_price_2 = float(checkout_product_prices[1].text.lstrip("$"))

    item_total_price = driver.find_element(
        By.CSS_SELECTOR, "#checkout_summary_container div.summary_subtotal_label"
    )

    item_total_price = get_price(item_total_price)

    tax_price = driver.find_element(
        By.CSS_SELECTOR, "#checkout_summary_container div.summary_tax_label"
    )
    tax_price = get_price(tax_price)

    total_price = driver.find_element(
        By.CSS_SELECTOR,
        "#checkout_summary_container div.summary_info_label.summary_total_label",
    )
    total_price = get_price(total_price)

    order_finish = driver.find_element(By.CSS_SELECTOR, "#finish")
    order_finish.click()

    complete = driver.find_element(By.CSS_SELECTOR, "#header_container div span")

    assert checkout_product_name_1 == buy_a_product_name_1
    assert checkout_product_name_2 == buy_a_product_name_2
    assert checkout_product_price_1 + checkout_product_price_2 == item_total_price
    assert round(item_total_price + tax_price, 2) == round(total_price, 2)
    assert complete.text == "Checkout: Complete!"

    driver.quit()
