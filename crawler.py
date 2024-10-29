import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

# 設定股票代號和年份
stock_code = "2317"
years = "112"

# 根據股票代號和年份創建資料夾
folder_path = os.path.join(f"Reports for {stock_code} in {years}")
os.makedirs(folder_path, exist_ok=True)

# 啟動 ChromeDriver
cservice = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=cservice)
wait = WebDriverWait(driver, 20)

# 開啟目標頁面
driver.get(f"https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id={stock_code}&year={years}&seamon=&mtype=A&")

# 找到所有 PDF 連結
pdf_links = driver.find_elements(By.XPATH, '//a[contains(@href, ".pdf")]')
pdf_links_lists = [link.text for link in pdf_links]

# 設置請求間的延遲
delay_between_requests = 10 

# 下載每個 PDF
for link_text in pdf_links_lists:
    driver.get(f"https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id={stock_code}&year={years}&seamon=&mtype=A&")

    try:
        link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
        link.click()

        wait.until(EC.new_window_is_opened)
        driver.switch_to.window(driver.window_handles[-1])

        second_pdf_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        second_pdf_link.click()

        # 下載 PDF 檔案
        response = requests.get(driver.current_url)
        with open(os.path.join(folder_path, f"{link_text}.pdf"), 'wb') as f:
            f.write(response.content)

        print(f"{link_text} downloaded successfully.")

    except Exception as e:
        print(f"Failed to download {link_text}: {e}")
    finally:
        time.sleep(delay_between_requests)

driver.quit()