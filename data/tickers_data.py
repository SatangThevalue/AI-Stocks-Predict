import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd
import logging

def get_data_all():
    #get_data_s_p_500()
    #get_data_market_th(name_set ="SET100")
    #get_data_market_th(name_set ="SET50")
    get_data_stock_th(name_set ="SET100")
    #get_data_stock_th(name_set ="SET50")


def get_data_s_p_500():
    import pandas as pd
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',index_col=0)[0]
    os.makedirs("./data/tickers_data/market/", exist_ok=True)
    tickers.to_csv(path_or_buf='./data/tickers_data/market/s_p_500.csv')
    logging.info('--- เก็บข้อมูลตลาด : S&P500  สำเร็จ!!! ---')



def get_data_market_th(name_set ="SET100"):
    data_df = pd.DataFrame()
    driver.get('https://www.set.or.th/en/market/index/'+ name_set +'/overview')
    ##ดึงตารางจากหน้าเว็บ
    data_df = pd.read_html(driver.page_source)[1]
    ##ลบคำว่า (Click to sort Ascending) ออก
    clean_columns = []
    for c in data_df.columns:
        clean_columns.append(c.replace('  (Click to sort Ascending)',''))
    data_df.columns = clean_columns
    ##ตั้งค่า set_index เป็น 'หลักทรัพย์'
    data_df = data_df.set_index('Symbol')
    data_df.columns = ['open', 'high', 'low', 'last', 'change', 'per_change', 'bid', 'offer',
       'volume', 'value']
    os.makedirs("./data/tickers_data/market/", exist_ok=True)
    full_file_name = './data/tickers_data/market/' + name_set + '.csv'
    data_df.to_csv(full_file_name)
    logging.info('--- เก็บข้อมูลตลาด : ' + name_set + ' สำเร็จ!!! ---')

def get_data_stock_th(name_set='SET50'):
    stock_df = pd.read_csv('./data/tickers_data/market/'+ name_set +'.csv',index_col='Symbol')
    for stock in stock_df.index:
        get_data_stock(stock)

def get_data_stock(stock):
    url = 'https://www.set.or.th/en/market/product/stock/quote/'+ stock +'/financial-statement/company-highlights'
    driver.get(url)
    stock_data = driver.page_source
    tmp_df = pd.read_html(stock_data)[0]
    os.makedirs("./data/tickers_data/stock/", exist_ok=True)
    tmp_df.to_csv('./data/tickers_data/stock/Financial_data_' + stock + '.csv')
    logging.info('--- เก็บข้อมูลหุ้น : ' + stock + ' สำเร็จ!!! ---')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    options = Options()
    #options.add_argument('headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    logging.info('--- โหลด Web Driver Chrome สำเร็จ!!! ---')
    get_data_all = get_data_all()
    driver.quit()
    logging.info('--- หยุดกระบวนการของ Web Driver Chrome : ทั้งหมด ---')
    
