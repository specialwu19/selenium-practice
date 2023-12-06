from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_success, get_driver
import time


driver = get_driver()


def test_add_product_into_cart_success():
    login_success(driver)

    homepage_ready = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

    pick_a_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    pick_a_product_1.click()
    time.sleep(1)
    buy_a_product_1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    buy_a_product_title_1 = driver.find_element(
        By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    )
    buy_a_product_name_1 = buy_a_product_title_1.text
    buy_a_product_1.click()
    time.sleep(1)

    back_to_homepage = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
    back_to_homepage.click()
    time.sleep(1)

    pick_a_product_2 = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
    pick_a_product_2.click()
    time.sleep(1)
    buy_a_product_2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    buy_a_product_title_2 = driver.find_element(
        By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    )
    buy_a_product_name_2 = buy_a_product_title_2.text
    buy_a_product_2.click()
    time.sleep(1)

    shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
    shopping_cart_nmber_2 = driver.find_element(
        By.XPATH, '//*[@id="shopping_cart_container"]/a/span'
    )
    shopping_cart_nmber = shopping_cart_nmber_2.text
    shopping_cart.click()

    shopping_cart_product_1 = driver.find_element(
        By.XPATH, '//*[@id="item_4_title_link"]/div'
    )
    shopping_cart_product_2 = driver.find_element(
        By.XPATH, '//*[@id="item_1_title_link"]/div'
    )

    assert buy_a_product_name_1 == shopping_cart_product_1.text
    assert buy_a_product_name_2 == shopping_cart_product_2.text
    assert shopping_cart_nmber == "2"


def test_remove_product_success():
    back_to_homepage = driver.find_element(By.ID, "continue-shopping")
    back_to_homepage.click()
    time.sleep(1)

    find_the_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img')
    find_the_product_1.click()

    remove_a_product_1 = driver.find_element(
        By.XPATH, '//*[@id="remove-sauce-labs-backpack"]'
    )
    remove_a_product_1.click()
    time.sleep(1)

    back_to_homepage = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
    back_to_homepage.click()
    time.sleep(1)

    find_the_product_2 = driver.find_element(By.XPATH, '//*[@id="item_1_img_link"]/img')
    find_the_product_2.click()

    remove_a_product_2 = driver.find_element(
        By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]'
    )
    remove_a_product_2.click()
    time.sleep(1)

    shopping_cart_nmber_0 = driver.find_element(
        By.XPATH, '//*[@id="shopping_cart_container"]/a'
    )

    assert shopping_cart_nmber_0.text == ""

    driver.quit()
