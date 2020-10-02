from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser = webdriver.Chrome()


def read_file(filename):
    file = open(filename + '.txt', 'r')
    result = [i.split(': ')[1].strip() for i in file]
    return result

def get_data(url):
    browser.get(url)
    time.sleep(2)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_headers(data_source):
    table_source = data_source.find_all('table')[0]
    table_head = table_source.find_all('thead')[0]
    columns = table_head.find_all('th')
    headers = [i.text for i in columns]
    return headers


def get_rows(data_source, col_count):
    all_rows = list()
    table_source = data_source.find_all('table')[0]
    table_body = table_source.find_all('tbody')[0]
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        cells = row.find_all('td')
        name = cells[0].find_all('div')[0].find_all('div')[0].text.split(',')[0]
        change = cells[col_count - 3].text
        if cells[col_count - 2].text.count('×') > 1:
            price_ex = cells[col_count - 2].text.split('×')[0]
            price_chaos = cells[col_count - 2].text.split('×')[1]
        else:
            price_ex = 'None'
            price_chaos = cells[col_count - 2].text.split('×')[0]

        all_rows.append([name, change, price_ex, price_chaos])

    return all_rows

def close_browser():
    browser.close()