import pytest
import allure
from playwright.sync_api import sync_playwright, Page,expect
import time


def test_vwo_Login():
    #initializing the browser and page
    browser = sync_playwright().start().chromium.launch(headless=False)
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page2 = context2.new_page()

    #interacting the web elements
    page1.goto("https://app.vwo.com")
    page2.goto("https://bing.com")
    time.sleep(6)
    page_title1 = page1.title()
    page_title2 = page2.title()
    print("page_title1", page_title1)
    print("page_title2", page_title2)
    context1.close()
    context2.close()
    browser.close()
