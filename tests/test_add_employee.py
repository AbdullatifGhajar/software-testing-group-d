from playwright.sync_api import expect, Page

from .employee import Employee, add_employee


def check_employee_name(page: Page, employee: Employee) -> None:
    page.goto("https://d.hr.dmerej.info/employees")

    # check if employee is in the list
    employee_cell = page.get_by_role("cell", name=employee.name, exact=True)
    expect(employee_cell).to_be_visible()


def test_employee_added(reset_db, page: Page):
    employee = Employee(
        name="John Doe",
        email="john@doe.com",
        address_line1="1 Main Street",
        address_line2="",
        city="New York",
        zip_code="10001",
        hiring_date="2021-01-01",
        job_title="Manager",
    )

    add_employee(page, employee)
    check_employee_name(page, employee)
