# 💰 Financial Report Crawler (TWSE 財務報告自動下載工具)

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Web%20Scraping-Selenium-green?style=flat-square&logo=selenium)](https://www.selenium.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

## 🌟 專案簡介 (Project Overview)

此專案是一個基於 **Python** 和 **Selenium** 開發的網路爬蟲工具，旨在自動化下載**台灣證券交易所 (TWSE)** 網站上的上市櫃公司年度財務報告 PDF 檔案。

本工具的開發源於金融業朋友的實際需求，解決了銀行或相關從業人員手動下載財報的**繁瑣流程**，大幅提升了資料蒐集的**效率與精確度**。

## 🎯 核心功能 (Features)

* **目標設定靈活：** 可透過編輯程式碼中的變數，輕鬆設定欲下載的**股票代碼**（例如：`2330`）與**民國年份**（例如：`112`）。
* **PDF 自動擷取：** 自動導航至 TWSE 報告頁面，精準抓取所有符合條件的 PDF 連結。
* **批次下載與本地保存：** 批量下載選定的財務報告，並依據股票代碼與年份，自動儲存至本地資料夾（命名格式：`Reports for <股票代碼> in <年份>`）。
* **延遲機制：** 內建下載間隔延遲（可調整），以避免對目標網站造成過多請求。

---

## 🛠 技術棧 (Tech Stack)

| 類別 | 工具/技術 | 說明 |
| :--- | :--- | :--- |
| **程式語言** | `Python` | 專案主要開發語言。 |
| **網頁自動化** | `Selenium` | 用於模擬瀏覽器行為，進行網頁導航與資料擷取。 |
| **環境管理** | `WebDriver Manager` | 自動管理和安裝 ChromeDriver，簡化環境設定。 |

## 🚀 環境需求與安裝 (Installation & Setup)

本專案使用 Python 3.x 版本，您需要先安裝所需的函式庫。

### 步驟 1: 克隆儲存庫

```bash
git clone Https://[github.com/TsengYuanChe/Financial_report_crawler.git](https://github.com/TsengYuanChe/Financial_report_crawler.git)
cd Financial_report_crawler
```

### 步驟 2: 安裝依賴函式庫

請確保您的系統已安裝 `pip`，並使用 `requirements.txt` 檔案來安裝所有必要的 Python 套件：

```bash
pip install -r requirements.txt
```

### 步驟 3: 準備 ChromeDriver

本專案利用 `WebDriver Manager` 自動安裝和配置 `ChromeDriver`，因此您**無需手動下載**。只需確保您的系統已安裝 **Chrome 瀏覽器**。

> **ℹ️ 關於 WebDriver Manager**
>
> `webdriver-manager` 是一個 Python 函式庫，它會在您第一次執行程式時，自動檢查並下載與您本地 Chrome 瀏覽器版本相符的 ChromeDriver，並將其設置為環境路徑。這大大簡化了 Selenium 爬蟲的環境設定步驟。

---

## 📖 使用方法 (Usage)

本工具的核心邏輯位於 `crawler.py` 檔案中。

### 1. 配置目標參數

開啟 `crawler.py` 檔案，修改以下兩個變數以設定您想要下載的股票代碼和年份：

```python
# 編輯此處的變數來設定您的目標
stock_code = "2330"   # 例如：台積電
years = "112"         # 例如：民國 112 年 (2023 年)
```

### 2. 執行程式

在終端機中執行主爬蟲程式：

```bash
python crawler.py
```

### 3. 查看輸出

程式執行完成後，所有下載的 PDF 檔案將會被儲存到當前目錄下以目標參數命名的資料夾中。

**輸出範例：**
```bash
./Reports for 2330 in 112/
```

---

## ⚠️ 注意事項 (Notes)

* **網站結構變更：** 如果台灣證券交易所的網頁結構或 URL 發生變化，這可能導致 `crawler.py` 中的 XPath 或選擇器失效，需要使用者手動更新程式碼以適應新的網頁結構。
* **連線延遲：** 程式中已設置每次下載間的延遲（例如 `time.sleep(2)`）。如果您的網路連線速度較慢或擔心對目標網站造成過多負擔，可以根據需求調整這個延遲時間。
* **瀏覽器要求：** 確保您的作業系統上已安裝 **Google Chrome 瀏覽器**，因為 `webdriver-manager` 預設會使用它。

---

## 📄 授權條款 (License)

本專案採用 **MIT 授權條款** 開源。詳情請參閱 [LICENSE](https://opensource.org/licenses/MIT) 文件。

