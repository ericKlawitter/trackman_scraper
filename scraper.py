import requests
from lxml import html
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlparse
from urllib.parse import parse_qs
from trackman_output import TrackmanOutput


import trackman_html_constants as div_id
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def process_row(row, date, report_id):
    club = row.find_element(By.CLASS_NAME, div_id.class_name_row_club_text).text
    stats_element = row.find_element(By.CLASS_NAME, div_id.class_name_stat_names)
    stats = [stat.text for stat in stats_element.find_elements(By.CLASS_NAME, div_id.class_name_stat_name)]
    output = TrackmanOutput(date, report_id, club)
    shots = row.find_elements(By.CLASS_NAME, div_id.class_name_shot_detail)
    for i, shot in enumerate(shots):
        # 0th Column is shot_num, 1st is visibility button, second is video, third is share
        shot_data = [td.text for i, td in enumerate(shot.find_elements(By.TAG_NAME, 'td')) if i > 3]
        data = dict(zip(stats, shot_data))
        data['ShotNum'] = str(i)
        data['Date'] = date
        data['ReportId'] = report_id
        output.add_shot(data)


    #averages_element = row.find_element(By.CLASS_NAME, div_id.class_name_shot_averages)
    # first column is label 'Average', second is share button
    #averages = [td.text for i, td in enumerate(averages_element.find_elements(By.TAG_NAME, 'td')) if i > 1]
    #print(averages)

    #std_dev_element = row.find_element(By.CLASS_NAME, div_id.class_name_shot_consistency)
    # first column is label 'Consistency'
    #std_devs = [td.text for i, td in enumerate(std_dev_element.find_elements(By.TAG_NAME, 'td')) if i > 0]
    #print(std_devs)
    
    output.write()


def scrape(url):
    report_id = parse_qs(urlparse(url).query)['r'][0]
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capa)
    driver.set_window_size(1440, 900)
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, div_id.class_name_date)))
    date = header.text.replace('/', '-')

    results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, div_id.class_name_results)))

    rows = results.find_elements(By.CLASS_NAME, div_id.class_name_results_table)
    for row in rows:
        process_row(row, date, report_id)
