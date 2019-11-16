import json
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_browser():
    chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(chrome_driver, options=options)
    return browser


def login(username, password):
    browser = get_browser()
    browser.get('http://202.103.199.210:8050/cas3/login')
    username_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'username'))
    )
    password_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'password'))
    )
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'submit'))
    )
    submit_input.click()
    print(browser.title)

    browser.get('http://202.103.199.210:8070/nnxmgl/nnxmgl/xmtb/xmxx/TzxmProjectbaseinfoListPage.jspx?type=30')
    browser_cookies = browser.get_cookies()
    cookies_str_lst = []
    for cookie in browser_cookies:
        cookie_str = '"{}","{}","{}",domain="{}"'.format(cookie['name'], cookie['value'], cookie['path'],
                                                         cookie['domain'])
        cookies_str_lst.append(cookie_str)
    with open('cookie.txt', 'w') as f:
        f.write(json.dumps(browser_cookies))

    all_project_id_lst = []
    while True:
        time.sleep(1)
        trs = WebDriverWait(browser,5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//tbody[@id="templateform:reFreshData_data"]/tr'))
        )
        # trs = browser.find_elements_by_xpath('//tbody[@id="templateform:reFreshData_data"]/tr')
        for tr in trs:
            guid_btn = tr.find_element_by_xpath('./td[4]/div/a')
            guid = guid_btn.get_attribute('onclick')
            re_str = r".*\((.*-.*-.*-.*-.*)?','"
            re_obj = re.match(re_str, guid)
            new_temp = re_obj.group(1)
            new_re_str = r"'(.*)','"
            guid = re.match(new_re_str, new_temp).group(1)
            all_project_id_lst.append(guid)
        next_btn = browser.find_element_by_xpath('//div[@class="ui-paginator-wrap"]/span[4]')
        if not next_btn.get_attribute('class') == "ui-paginator-next ui-state-default ui-corner-all ui-state-disabled":
            next_btn.click()
        else:
            break

    for i in all_project_id_lst:
        edit_url = "http://202.103.199.210:8070/nnxmgl/nnxmgl/xmtb/xmxx/TzxmProjectEditAllinfo.jspx?guid={}".format(i)
        browser.get(edit_url)
        project_name = browser.find_element_by_id('templateform:accordion1:projname').get_attribute('value')
        print(project_name)
        pass

    return browser_cookies, cookies_str_lst, 'cookie.txt', all_project_id_lst


if __name__ == '__main__':
    cookies, cookie_str_lst, cookie_file, total_guid_lst = login('wxjtj', '11111')
