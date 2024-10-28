from playwright.sync_api import sync_playwright
import re

def extracting_p_and_blockquote_tags(driver):
    div_tag = driver.query_selector("xpath = //div[@class = 'judgments']")
    all_tags = div_tag.query_selector_all("*")
    req_tags = []
    for tag in all_tags:
        if tag.evaluate("element => element.tagName").lower() == 'p' or tag.evaluate("element => element.tagName").lower() == 'blockquote':
            req_tags.append(tag)
    return req_tags

#remove_starting_nums
def remove_starting_nums(str):
    return re.sub(r'^\d+.', '', str)

#Extracting input_ids of each case
def extract_input_id(req_tags):
    input_id = ''
    titles = ["Fact", "Issue"]
    for tag in req_tags:
        if tag.get_attribute('title') in titles:
            if tag.evaluate("element => element.tagName").lower() == 'blockquote':
                input_id += tag.inner_text() + "\n"
            elif tag.evaluate("element => element.tagName").lower() == 'p':
                s = remove_starting_nums(tag.inner_text())
                input_id += s + "\n"
    return input_id

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
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        driver = browser.new_page()
        driver.goto(url)
        req_tags = extracting_p_and_blockquote_tags(driver)
        input_id = extract_input_id(req_tags)
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