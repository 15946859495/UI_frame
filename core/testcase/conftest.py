import time

import allure
import pytest
from core.until.funcs import is_login, load_cookies, save_cookies
from webdriver_helper import get_webdriver
from selenium import webdriver
from core.pages import IndexPage
from core.until.settings import settings


@pytest.fixture(scope="module")
def driver():
    chrome_options = webdriver.ChromeOptions()  # 创建chrome_options对象
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options = chrome_options
    driver = get_webdriver(settings["driver_type"], options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()  # 关闭浏览器


# @pytest.fixture(scope="session", autouse=True)
# def narcotic_init():
#     yield
#     print('\nUI自动化测试用例 执行结束...\n')


@pytest.fixture(scope="session")
def admin_driver():
    """已登录的浏览器，以便快速执行用例"""
    chrome_options = webdriver.ChromeOptions()  # 创建chrome_options对象
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options = chrome_options
    driver = get_webdriver(settings["driver_type"], options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    load_cookies(driver)

    # 判断：只有未登录，才执行登录流程
    if is_login(driver) is False:
        page = IndexPage(driver)
        assert page.admin_login("19542812247", "LEdiiUpV", 'https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr') is True

    yield driver

    save_cookies(driver)
    time.sleep(1)
    driver.quit()
