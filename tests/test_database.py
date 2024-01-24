from playwright.sync_api import Page, expect

def test_employee_list_empty(reset_db, page: Page):
    page.goto("https://d.hr.dmerej.info/employees")
    expect(page.get_by_text("Home Employees No employees")).to_be_visible()


