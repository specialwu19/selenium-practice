from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import login_success, get_driver


driver = get_driver()


def test_login_success():
    login_success(driver)

    login_successful = driver.find_element(By.CSS_SELECTOR, ".app_logo")

    assert login_successful.text == "Swag Labs"


def test_logout_success():
    function_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#react-burger-menu-btn"))
    )
    function_button.click()
    time.sleep(1)
    logout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#logout_sidebar_link"))
    )
    logout.click()
    logout_success = driver.find_element(By.CSS_SELECTOR, "#login-button")
    time.sleep(1)

    assert logout_success.get_attribute("value") == "Login"

    driver.quit()
