# Same automation in Selenium
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_carlos_is_on_leadership_page_with_selenium(driver_setup):
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://www.paloaltonetworks.com/')

    # hover About link
    about_link = driver.find_element(By.CSS_SELECTOR, 'a[id="nav_solutions"]')
    actions = ActionChains(driver)
    actions.move_to_element(about_link).perform()

    # click on get started from menu
    wait.until(EC._element_if_visible(By.CSS_SELECTOR, 'a[href="/get-started"')).click()

    # check if 'Text' is on the page
    assert wait.until(lambda _: driver.find_element(By.XPATH, "//*[contains(text(), 'Future-proof your security with reliable solutions, today')]"))