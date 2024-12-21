import time, re
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

import pickle

with open('hanja.pkl', 'rb') as f:
    hanja = pickle.load(f)

with open('kor.pkl', 'rb') as f:
    kor = pickle.load(f)
with open('meaning.pkl', 'rb') as f:
    meaning = pickle.load(f)
with open('url.pkl', 'rb') as f:
    url = pickle.load(f)

path = "https://hanja.dict.naver.com/"
for i in range(1,135):
    print("PAGE_" + str(i))

    bPath = path + "#/category/subject?t=1&page=" + str(i)

    driver.get(bPath)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    href = soup.select("#content > div > div.component_keyword.my_component_keyword.has-saving-function > div.row")

    for k in range(len(href)):
        dUrl = href[k].select_one('a').get('href')
        dPath = path + dUrl
        
        driver.get(dPath)
        time.sleep(3)

        soup_detail = BeautifulSoup(driver.page_source, 'html.parser')
        base = soup_detail.select_one("#content > div.section.section_entry._section_entry > div > div.entry_title._guide_lang")

        hanja_content = base.select("strong > span > span")
        hanja_content = ''.join(hanjas.text for hanjas in hanja_content)
        hanja.append(hanja_content)

        kor_content = base.select_one("div > div.mean").text

        meaning_list = []
        mean_content = soup_detail.select("#content > div.article._article.is-closed > div.section.section_mean.is-source._section_mean._data_index_1 > div > div.mean_tray > ul > li")
         
        for l in range(len(mean_content)):
            mean_content_detail = mean_content[l].select("div.mean_desc > div > span")
            mean_content_detail = ''.join(m.text for m in mean_content_detail)
            meaning_list.append(re.sub("[^ 가-힣ㄱ-ㅎㅏ-ㅣ.,‘’]", '', mean_content_detail))

        print(kor_content, end = ' ')
        hanja.append(hanja_content)
        kor.append(kor_content)
        meaning.append(meaning_list)
        url.append(dUrl[13:])

with open('hanja.pkl', 'wb') as f:
    pickle.dump(hanja, f)
with open('kor.pkl', 'wb') as f:
    pickle.dump(kor, f)
with open('meaning.pkl', 'wb') as f:
    pickle.dump(meaning, f)
with open('url.pkl', 'wb') as f:
    pickle.dump(url, f)