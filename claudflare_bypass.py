from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

######################## options for cloudflare bypass ###############################
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

###################### start the browser ###############################
driver = webdriver.Chrome(options=options) 
driver.maximize_window()
driver.execute_script("window.open('https://www.sahibinden.com/kategori/emlak', '_blank')")
sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.frame(0)
driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input').click()
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.window(driver.window_handles[1])

################## fill the form ###############################
sleep(5)
city_dd = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[1]/div[2]/div[1]/div/span')
city_dd.click()


tekirdag = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[1]/div[2]/div[1]/div/ul/div/div[1]/li[74]")
driver.execute_script("arguments[0].scrollIntoView()", tekirdag)
tekirdag.click()

driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[2]/div[3]/a[1]').click()


# wait = WebDriverWait(driver, 10)
# city_dd = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[1]/div[2]/div[1]/div')))
# city_dd.click()


# driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[1]/div[2]/div[1]/div/ul/div/div[1]/li[74]').click()
# driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[2]/div[3]/a[1]').click()
# /html/body/div[5]/div[1]/div[2]/div/div/form[1]/div/div[1]/div[2]/div[1]/div


# driver.find_element(By.CSS_SELECTOR, "a.prevNextBut[title='Sonraki']") 
urls = driver.find_elements(By.CSS_SELECTOR, 'tr.searchResultsItem:not(.searchResultsPromoSuper):not(.nativeAd) td:nth-child(1) a')
url_lst = [url.get_attribute('href') for url in urls]
print(url_lst)
driver.find_element(By.CSS_SELECTOR, "div#onetrust-close-btn-container").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "div.feature-discovery__icon-circle").click()

for i in range(49):
    driver.find_element(By.CSS_SELECTOR, "a.prevNextBut[title='Sonraki']").click()
    sleep(4)
    urls = driver.find_elements(By.CSS_SELECTOR, 'tr.searchResultsItem:not(.searchResultsPromoSuper):not(.nativeAd) td:nth-child(1) a')
    url_lst += [url.get_attribute('href') for url in urls]

################## save the urls to a file ###############################
current_directory = os.getcwd()
file_name = "urls.txt"
file_path = os.path.join(current_directory, file_name)

with open(file_path, "w") as file:
    for url in url_lst:
        file.write(url + "\n")

print(f"File saved at: {file_path}")



# sleep(3)
# city = Select(city_dd)

# cities = city.options

# for c in cities:
#     print(c.text)

