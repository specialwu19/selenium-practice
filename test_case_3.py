from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver
import time


driver = get_driver()


def test_login_fail():
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user-name"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    username.send_keys("abc123")
    password.send_keys("abcdefg")

    login = driver.find_element(By.NAME, "login-button")
    login.click()
    time.sleep(1)

    login_fail = driver.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'
    )

    assert (
        login_fail.text
        == "Epic sadface: Username and password do not match any user in this service"
    )

    driver.quit()
