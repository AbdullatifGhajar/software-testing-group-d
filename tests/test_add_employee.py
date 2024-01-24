from playwright.sync_api import expect, Page

from .employee import Employee, EmployeePage, BasicInfo, Address, Contract


def test_add_employee(reset_db, page: Page):
    employee = Employee(
        BasicInfo(
            name="John Doe",
            email="john@doe.come",
        ),
        Address(
            address_line1="1 Main Street",
            address_line2="",
            city="New York",
            zip_code="11111",
        ),
        Contract(
            hiring_date="2021-01-01",
            job_title="Software Engineer",
        ),
    )

    employee_page = EmployeePage(page)
    employee_page.add_employee(employee)
    assert employee_page.is_employee_in_employee_list(employee)


def test_zip_code_is_str(reset_db, page: Page):
    employee = Employee(
        BasicInfo(
            name="John Doe",
            email="john@doe.come",
        ),
        Address(
            address_line1="1 Main Street",
            address_line2="",
            city="New York",
            zip_code="00000",
        ),
        Contract(
            hiring_date="2021-01-01",
            job_title="Software Engineer",
        ),
    )

    employee_page = EmployeePage(page)
    employee_page.add_employee(employee)

    saved_zip_code = employee_page.saved_address(employee).zip_code
    assert saved_zip_code == employee.address.zip_code
