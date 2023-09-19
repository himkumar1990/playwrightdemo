from playwright.async_api import Page, expect
import time

def test_checkbox_select(page: Page):
    page.goto("https://demoqa.com/checkbox")
    home_checkbox = page.locator(".rct-checkbox")
    assert home_checkbox.is_checked() is False

    # Check the checkbox
    home_checkbox.check()
    # Assert the checked state
    assert home_checkbox.is_checked() is True
    page.close()


def test_hover_over_element(page: Page):
    page.goto("https://demoqa.com/tool-tips")
    hover_over_me = page.locator("button#toolTipButton")
    hover_over_me.hover()
    time.sleep(2)
    hover_over_text = page.locator(".tooltip-inner")

    assert hover_over_text.is_visible() is True
