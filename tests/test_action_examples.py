from playwright.async_api import Page


def test_checkbox_select(page: Page):
    page.goto("https://demoqa.com/checkbox")
    home_checkbox = page.locator(".rct-checkbox")
    assert home_checkbox.is_checked() is False
    home_checkbox.check()
    assert home_checkbox.is_checked() is True
    page.close()
