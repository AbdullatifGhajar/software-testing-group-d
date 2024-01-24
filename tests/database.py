from playwright.sync_api import Page

def is_employee_list_empty(page: Page) -> bool:
    page.goto("https://d.hr.dmerej.info/employees")
    return page.get_by_text("Home Employees No employees").is_visible()


