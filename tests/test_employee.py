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

    saved_zip_code = employee_page.saved_address_on_page(employee).zip_code
    assert saved_zip_code == employee.address.zip_code


def test_edit_employee_address(reset_db, page: Page):
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
    new_address =  Address(
        address_line1="2 Main Street",
        address_line2="Building 2, Apt 3",
        city="New York",
        zip_code="11111",
    )

    employee_page.edit_employee_address(employee, new_address)

    saved_address = employee_page.saved_address_on_page(employee)
    
    assert saved_address.address_line1 == new_address.address_line1
    assert saved_address.address_line2 == new_address.address_line2

