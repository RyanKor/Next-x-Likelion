from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


print("Naver Crawling")
driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.naver.com")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
ranks = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

texts = []
cnt=0
for title in ranks:
    cnt += 1
    print(str(cnt) + '. ' + title.text.strip())

driver.quit()