import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
import time


@pytest.fixture(autouse=True)
def before_each_after_each(page: Page):
    print("print it before each test")
    context = page.context
    context.tracing.start(screenshots=True, snapshots=True)
    yield
    print("after each test.....")
    context.tracing.stop(path="trace.zip")


def test_001(page: Page):
    page.goto("https://demoqa.com/text-box")
    full_name = page.get_by_placeholder("Full Name")
    email = page.get_by_placeholder("name@example.com")
    address = page.get_by_role("textbox", name="address")
    permanent_address = page.locator("#permanentAddress")

    # using locator.fill method to fill out form fields
    # It works for <input>, <textarea> and [contenteditable] elements.
    full_name.fill("Himanshu Kumar")
    email.fill("testemail@gmail.com")
    address.fill("first street 10")
    permanent_address.fill("second street 20")
    page.get_by_text("Submit").click()
    time.sleep(2)

    result_name = page.locator("#name")
    result_address = page.locator("p#currentAddress")

    expect(result_name).to_have_text("Name:Himanshu Kumar")
    expect(result_address).to_have_text("Current Address :first street 10")


def test_002(page: Page):
    page.goto("https://demoqa.com/links")
    context = page.context
    with context.expect_page() as home_page_info:
        page.locator("//a[@id ='simpleLink']").click()
    new_page = home_page_info.value

    new_page.wait_for_load_state()
    print("Title of new page: " + new_page.title())


