from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import re

def extracting_p_and_blockquote_tags(driver):
    div_tag = driver.find("div", class_ = 'judgments')
    req_tags = []
    for tag in div_tag:
        if tag.name == 'p' or tag.name == 'blockquote':
            req_tags.append(tag)
    return extract_input_id(req_tags)

#remove_starting_nums
def remove_starting_nums(str):
    return re.sub(r'^\d+.', '', str)

#Extracting input_ids of each case
def extract_input_id(req_tags):
    input_id = ''
    try:
        titles = ["Fact", "Issue"]
        for tag in req_tags:
            if tag['title'] in titles:
                if tag.name == 'blockquote':
                    input_id += tag.text + "\n"
                elif tag.name == 'p':
                    s = remove_starting_nums(tag.text)
                    input_id += s + "\n"
        return input_id
    except:
        return 

#Extracting input_ids of each case
def extract_label(req_tags):
    req_tags = req_tags
    label = ''
    titles = ["Court's Reasoning", "Analysis of the law", "Precedent Analysis", "Conclusion"]
    for tag in req_tags:
        if tag.get('title') in titles:
            if tag.name == 'blockquote':
                label += tag.text + "\n"
            elif tag.name == 'p':
                #s = remove_starting_nums(tag.text)
                #label += s + "\n"
                label += tag.text + "\n"
    return label

def driver_start(url):
    #selenium headless mode
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options = options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    input_id = extracting_p_and_blockquote_tags(soup)
    print(input_id)

urls = [
    'https://indiankanoon.org/docfragment/161945704/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-1017%20todate%3A%2031-12-1017',
'https://indiankanoon.org/docfragment/178502756/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-1017%20todate%3A%2031-12-1017',
'https://indiankanoon.org/docfragment/181152695/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-1017%20todate%3A%2031-12-1017',
'https://indiankanoon.org/docfragment/163162687/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-1017%20todate%3A%2031-12-1017',
'https://indiankanoon.org/docfragment/1372045/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-1800%20todate%3A%2031-12-1800'
]

for url in urls:
    driver_start(url)
    print("\n\n---------------------------------------\n\n")
    break