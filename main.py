from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
browser.get('https://sbis.ru/')


def clck_bttn():
    click_button = (browser.find_element(By.XPATH,
                                         value='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div['
                                               '2]/ul/li[3]/a'))
    click_button.click()


browser.switch_to.window(browser.window_handles[-1])


def my_reg():
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')))

    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]')))


def change_reg():
    click_button2 = (
        browser.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div['
                                             '2]/span/span'))
    click_button2.click()

    wait = WebDriverWait(browser, 10)
    element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div['
                                                                   '2]/div/ul/li[43]/span')))
    element.click()


def check_reg():
    WebDriverWait(browser, 10).until(ec.title_contains("СБИС Контакты — Камчатский край"))
    print(browser.title)

    print(f'Currently URL is: {browser.current_url}')

    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')))

    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')))
