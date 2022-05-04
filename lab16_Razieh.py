import datetime

from selenium import webdriver # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)

#-------- DATA PARAMETERS ----------------
app = 'STORE'
PS_navigate_url = 'https://www.demoblaze.com/'
PS_home_page_title = 'STORE'
PS_home_page_url = 'https://www.demoblaze.com/'

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
    if driver.current_url == PS_home_page_url and driver.title == PS_home_page_title:
        print(f'Yey! {app} App website launched successfully :)')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print(f'---------------***----------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()  # kill the instance


def shopping():
    if driver.current_url == PS_home_page_url: # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//h2[contains(., "Nexus 6")]').is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        sleep(0.25)
        driver.switch_to.alert.accept()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Cart').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//td[contains(., "Nexus 6")]').is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Delete').click()




# Launch app
setUp()
# shopping process
shopping()
# Close app
tearDown()
