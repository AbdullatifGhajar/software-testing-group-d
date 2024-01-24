from playwright.sync_api import Page

def reset_database(page: Page):
    page.goto("https://d.hr.dmerej.info/")
    page.get_by_role("link", name="Reset database").click()
    page.get_by_role("button", name="Proceed").click()

def is_employee_list_empty(page: Page) -> bool:
    page.goto("https://d.hr.dmerej.info/employees")
    return page.get_by_text("Home Employees No employees").is_visible()


