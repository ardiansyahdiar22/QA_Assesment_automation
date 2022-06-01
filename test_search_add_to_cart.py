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

def test_search_product(main):
    # ===== Login Process =====
    main.find_element(By.XPATH, '//*[@id="menu-1-b1a0ff7"]/li[1]/a').click()
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[1]/span[2]/input').send_keys('6281223334444')
    time.sleep(3)
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[2]/span[2]/input').send_keys('password')

    # ====== Search Product Process =====
    main.find_element(By.XPATH, '//button[@class="btn btn--brand btn--block btn--large"]').click()
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/a[1]/span').click()
    
    time.sleep(3)
    main.find_element(By.XPATH, '//input[@class="appHeading__search__input"]').send_keys('kemeja')
    
    action = main.find_element(By.XPATH, '//input[@class="appHeading__search__input"]')
    action.send_keys(Keys.ENTER)

    time.sleep(3)
    title = main.title
    assert 'Evermos' in title

def test_add_to_cart(main):
    # ===== Login Process =====
    main.find_element(By.XPATH, '//*[@id="menu-1-b1a0ff7"]/li[1]/a').click()
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[1]/span[2]/input').send_keys('6281223334444')
    time.sleep(3)
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/form/label[2]/span[2]/input').send_keys('password')

    # ====== Search Product Process =====
    main.find_element(By.XPATH, '//button[@class="btn btn--brand btn--block btn--large"]').click()
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/a[1]/span').click()
    
    time.sleep(3)
    main.find_element(By.XPATH, '//input[@class="appHeading__search__input"]').send_keys('kemeja')
    
    action = main.find_element(By.XPATH, '//input[@class="appHeading__search__input"]')
    action.send_keys(Keys.ENTER)

    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div[1]/div[1]/div/div[1]/div[1]/a/img').click()
    main.find_element(By.XPATH, '//a[@class="productView__action__button btn--brand"]').click()

    time.sleep(3)
    main.find_element(By.XPATH, '//*[@id="__layout"]/div/div[5]/div/div[2]/div[1]/div[2]/div/label/div[1]/input').click()
    main.find_element(By.XPATH, '//button[@class="btn btn--brand btn--large btn--block"]').click()

    time.sleep(3)
    message = main.find_element(By.XPATH, '//div[@class="appDialog__message"]').text
    assert 'Produk berhasil ditambahkan ke keranjang' in message