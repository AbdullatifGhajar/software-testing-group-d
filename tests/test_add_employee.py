from playwright.sync_api import Playwright, sync_playwright, expect, Page


def add_employee(page: Page, employee_name: str) -> None:
    page.goto("https://d.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(employee_name)
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

def check_employee(page: Page, employee_name: str) -> None:
    page.goto("https://d.hr.dmerej.info/employees")
    
    # check if employee is in the list
    employee_row = page.get_by_role("cell", name=employee_name, exact=True)
    expect(employee_row).to_be_visible()


def test_employee_added():
    employee_name = "Pauline"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        add_employee(page, employee_name)
        check_employee(page, employee_name)

        context.close()
        browser.close()





