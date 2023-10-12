from playwright.sync_api import sync_playwright
import time


def test_shadow_locator():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://books-pwakit.appspot.com/")
    search_book = page.locator("input#input")
    search_book.fill("learn statistics")
    text_to_verify = page.locator(".books-desc")
    text_value = text_to_verify.text_content()
    print(text_value)
    assert text_value == "Search the world's most comprehensive index of full-text books."
    time.sleep(3)
    page.close()
    context.close()
