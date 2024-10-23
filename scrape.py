import time

import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("Pingaaaa")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()
        print("Closing Website")


def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find("body")
    if body:
        return str(body)
    else:
        return ""


def clean_body_content(body):
    soup = BeautifulSoup(body, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip() #remove any random back slashed n chars that are not between any chars.
    )
    return cleaned_content

def split_doom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length) # This for loop says for i in range of 0 starting point size of dom content and steps of 6000 we are making splits with this data.
    ]