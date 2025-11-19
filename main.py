import requests
from bs4 import BeautifulSoup
import pandas as pd
import time, random

EXCEL_PATH="./Parts_DataSheet_Links.xlsx"

BASE_URL="https://www.analog.com/jp/search.html?query={}"

HEADERS = {  # 模拟浏览器请求头
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0 Safari/537.36"
}

df = pd.read_excel(EXCEL_PATH)
df["datasheet_url"]=""

for idx,row in df.iterrows():
    kw = row.iloc[1]
    print(f"Working on {kw}")
    if pd.isna(kw) or str(kw).strip() == "" :
        print(f"")
        continue
    search_url = BASE_URL.format(kw)
    try:
        print(f"Getting data from {search_url}")
        response = requests.get(search_url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            print(f"Error getting data from {search_url}")
            datasheet_links.append("Failed to get data from {search_url}")
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        #result container
        result_container = soup.select_one("div", class_=".search-results__search-panel__results__analog")
        if not result_container:
            print("no result container found")

    except Exception as e:
        print(f"Error getting data from {search_url}")

if __name__ == "__main__":
    print(keywords)
