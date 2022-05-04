import datetime

from selenium import webdriver # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select

s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)

#-------- DATA PARAMETERS ----------------
app = 'STORE'
PS_navigate_url = 'https://www.demoblaze.com/'
PS_home_page_title = 'STORE'
PS_home_page_url = 'https://www.demoblaze.com/index.html'
products = ['Nexus 6', 'Sony xperia z5', 'Samsung galaxy s6']
#--------------------------------------------------------


def setUp():
    print(f'Launch {app} App')
    print(f'----------------***-----------------')
    # make browser full screen
    driver.maximize_window()

    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # navigate to App website
    driver.get(PS_navigate_url)

    # check that URL and the home page title are as expected
    if driver.current_url == PS_navigate_url and driver.title == PS_home_page_title:
        print(f'Yey! {app} App website launched successfully :)')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print('---------------***-------'
              '---------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()  # kill the instance


def shopping():
    if driver.current_url == PS_navigate_url: # check we are on the home page
        for item in products:
            driver.find_element(By.LINK_TEXT, item).click()
            sleep(0.25)
            assert driver.find_element(By.XPATH, '//h2[contains(., item)]').is_displayed()
            sleep(0.25)
            driver.find_element(By.LINK_TEXT, 'Add to cart').click()
            sleep(0.5)
            driver.switch_to.alert.accept()
            sleep(0.5)
            driver.find_element(By.ID, 'nava').click()
            assert driver.current_url == PS_home_page_url




def delete():
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    sleep(0.25)
    print(f'There are {len(products)} items in your cart:')
    for i in range(len(products)):
        assert driver.find_element(By.XPATH, '//a[contains(text(), i)]').is_displayed()
        print(f'{i+1}: {products[i]}')
        sleep(0.25)
    deleted_item = driver.find_element(By.XPATH, '//tr[2]//td[2]').text
    driver.find_element(By.XPATH, '//tr[2]//a[contains(text(), "Delete")]').click()
    print(f'{deleted_item} was second item in the cart and is deleted successfully!')






setUp()
shopping()
delete()
tearDown()
