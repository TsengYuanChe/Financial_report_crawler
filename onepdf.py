from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests

cservice = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=cservice)

wait = WebDriverWait(driver, 10)

driver.get("https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=2330&year=112&seamon=&mtype=A&")
link = driver.find_element(By.LINK_TEXT,'202301_2330_AI1.pdf')
link.click()

wait.until(EC.new_window_is_opened)
driver.switch_to.window(driver.window_handles[-1])

second_pdf_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '202301_2330_AI1.pdf')))
second_pdf_link.click()
response = requests.get(driver.current_url)
with open("2330/test11.pdf", 'wb') as f:
    f.write(response.content)

driver.quit()