import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def check(browser, selector_css):
    try:
        browser.find_element(By.CSS_SELECTOR, selector_css)
    except:
        return False
    return True


def test_button(browser):
    browser.get(link)
    assert check(browser, 'button.btn-add-to-basket[type="submit"]'), "нет кнопки добавить в корзину"