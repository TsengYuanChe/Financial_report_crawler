import requests
pdf_url = "https://doc.twse.com.tw/pdf/202301_2330_AI1_20240513_171531.pdf"
response = requests.get(pdf_url)
if response.status_code == 200:
    with open("2330/test.pdf","wb") as f:
        f.write(response.content)
    print("succees")
else:
    print("fail")
