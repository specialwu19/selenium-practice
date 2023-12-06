from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


browser = "chrome"
# browser = "firefox"
# browser = "edge"


def login_success(d):
    username = WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.NAME, "user-name"))
    )
    password = WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login = d.find_element(By.NAME, "login-button")
    login.click()


def get_driver():
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.saucedemo.com/")
        return driver

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get("https://www.saucedemo.com/")
        return driver

    # elif browser == "edge":

    else:
        raise KeyError("尚未支援的driver")
