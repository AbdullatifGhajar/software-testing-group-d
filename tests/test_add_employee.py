from playwright.sync_api import expect, Page

from .employee import Employee, add_employee


def is_employee_in_employee_list(page: Page, employee: Employee) -> None:
    page.goto("https://d.hr.dmerej.info/employees")

    # check if employee is in the list
    employee_cell = page.get_by_role("cell", name=employee.name, exact=True)
    expect(employee_cell).to_be_visible()


def test_add_employee(reset_db, page: Page):
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
    is_employee_in_employee_list(page, employee)

def check_employee_correct_zip_code(page: Page, employee: Employee):
    page.goto("https://d.hr.dmerej.info/employees")

    page.get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Update address").click()

    zip_code_on_page = page.get_by_placeholder("Zip code").get_attribute("value")
    assert zip_code_on_page == employee.zip_code


def test_zip_code_is_str(reset_db, page: Page):
    employee = Employee(
        name="John Doe",
        email="john@doe.com",
        address_line1="1 Main Street",
        address_line2="",
        city="New York",
        zip_code="00000",
        hiring_date="2021-01-01",
        job_title="Manager",
    )

    add_employee(page, employee)
    check_employee_correct_zip_code(page, employee)




