from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://d.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Pauline")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("pauline@gmail.com")
    page.get_by_role("button", name="Add").click()
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("25 ")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("Cool")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("11111111")
    page.get_by_role("group", name="Contract").click()
    page.get_by_placeholder("Hiring date").fill("2024-01-25")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("Test Job")
    page.get_by_role("button", name="Add").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
