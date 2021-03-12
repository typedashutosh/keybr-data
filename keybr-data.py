from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
speed = []
driver.get("https://www.keybr.com/profile/e316hty")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for s in soup.findAll('span', attrs={'class': 'StatisticList-itemValue'}):
    value = s.text
    speed.append(value)
df = pd.DataFrame(
    {'Speed': speed})
df.to_csv('speed.csv', index=False, encoding='utf-8')
