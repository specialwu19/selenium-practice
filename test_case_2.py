from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver
import time

driver = get_driver()


def test_login_fail():
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#password"))
    )

    username.send_keys("standard_user")
    password.send_keys("password")

    login = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login.click()
    time.sleep(1)

    login_fail = driver.find_element(
        By.CSS_SELECTOR, "div.error-message-container h3[data-test='error']"
    )

    assert (
        login_fail.text
        == "Epic sadface: Username and password do not match any user in this service"
    )

    driver.quit()
