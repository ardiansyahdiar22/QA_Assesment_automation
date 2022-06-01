import pytest 
import time
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture()
def main():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://evermos.com/home/')
    yield driver
    driver.quit()

def test_negatif_login(main):
    # ===== Login Process =====
    main.find_element(By.XPATH, '//*[@id="menu-1-b1a0ff7"]/li[1]/a').click()
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[1]/span[2]/input').send_keys('6281223334444')
    time.sleep(3)
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[2]/span[2]/input').send_keys('passwor')
    main.find_element(By.XPATH, '//button[@class="btn btn--brand btn--block btn--large"]').click()

    time.sleep(3)
    message = main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/p').text
    assert 'Nomor Telepon atau Kata Sandi anda salah!' in message

def test_negatif_login_2(main):
    # ===== Login Process =====
    main.find_element(By.XPATH, '//*[@id="menu-1-b1a0ff7"]/li[1]/a').click()
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[1]/span[2]/input').send_keys('628122333444')
    time.sleep(3)
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[2]/span[2]/input').send_keys('password')
    main.find_element(By.XPATH, '//button[@class="btn btn--brand btn--block btn--large"]').click()

    time.sleep(3)
    message = main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/p').text
    assert 'Nomor ini belum terdaftar sebagai reseller' in message

