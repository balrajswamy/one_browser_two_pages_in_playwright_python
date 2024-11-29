import pytest
import allure
from playwright.sync_api import sync_playwright, Page,expect


def test_vwo_Login():
    #initializing the browser and page
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #interacting the web elements
    page.goto("https://app.vwo.com")
    breakpoint()
    actual_title = page.title()
    expected_title = "Login - VWO"
    #validation portion
    expect(page).to_have_title(expected_title)