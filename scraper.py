import requests
from lxml import html
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import trackman_html_constants as div_id
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def html_parse_tree(url):
    page = requests.get(url)
    return html.fromstring(page.content)

def xpath_parse(tree, xpath):
    return tree.xpath(xpath)

def process_row(row):
    club = row.find_element(By.CLASS_NAME, div_id.class_name_row_club_text).text
    print(club)
    stats_element = row.find_element(By.CLASS_NAME, div_id.class_name_stat_names)
    stats = [stat.text for stat in stats_element.find_elements(By.CLASS_NAME, div_id.class_name_stat_name)]
    print(stats)
    shots = len(row.find_elements(By.CLASS_NAME, div_id.class_name_shot_detail))
    print(shots)

    averages_element = row.find_element(By.CLASS_NAME, div_id.class_name_shot_averages)
    # first column is label 'Average', second is share button
    averages = [td.text for i, td in enumerate(averages_element.find_elements(By.TAG_NAME, 'td')) if i > 1]
    print(averages)

    std_dev_element = row.find_element(By.CLASS_NAME, div_id.class_name_shot_consistency)
    # first column is label 'Consistency'
    std_devs = [td.text for i, td in enumerate(std_dev_element.find_elements(By.TAG_NAME, 'td')) if i > 0]
    print(std_devs)


def scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capa)
    driver.set_window_size(1440, 900)
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, div_id.class_name_results)))
    print(dir(results))

    rows = results.find_elements(By.CLASS_NAME, div_id.class_name_results_table)
    for row in rows:
        process_row(row)
