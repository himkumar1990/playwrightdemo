from playwright.sync_api import sync_playwright


def test_002():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.add_init_script(path="preload.js")

    page = context.new_page()
    page.goto("https://www.google.com")

    page.close()
    context.close()
