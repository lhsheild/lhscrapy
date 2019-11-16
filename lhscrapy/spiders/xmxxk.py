# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class XmxxkSpider(scrapy.Spider):
    name = 'xmxxk'
    allowed_domains = ['202.103.199.210:8050', '202.103.199.210:80']
    start_urls = ['http://202.103.199.210:8070/nnxmgl/nnwebsite/index.jspx']
    # chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # options = webdriver.ChromeOptions()
    # # options.add_argument('--headless')
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # browser = webdriver.Chrome(chrome_driver, options=options)

    def start_requests(self):
        chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        browser = webdriver.Chrome(chrome_driver, options=options)
        browser.get('http://202.103.199.210:8070/nnxmgl/nnwebsite/index.jspx')
        username_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'username'))
        )
        password_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )
        username_input.send_keys('wxjtj')
        password_input.send_keys('11111')
        submit_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit'))
        )
        submit_input.click()
        print(browser.title)
        cookies = browser.get_cookies()
        cookie_str_lst = []
        for cookie in cookies:
            cookie_str = '"{}","{}","{}",domain="{}"'.format(cookie['name'], cookie['value'], cookie['path'], cookie)
            cookie_str_lst.append(cookie_str)
        pass