from dataclasses import dataclass

from playwright.sync_api import Page

from .team import Team

@dataclass
class BasicInfo:
    name: str
    email: str

@dataclass
class Address:
    address_line1: str
    address_line2: str
    city: str
    zip_code: str

@dataclass
class Contract:
    hiring_date: str
    job_title: str

@dataclass
class Employee:
    basic_info: BasicInfo
    address: Address
    contract: Contract
    is_manager: bool = False
    # TODO: add team


class EmployeePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_employee_list_page(self):
        self.page.goto("https://d.hr.dmerej.info/employees")

    def navigate_to_add_employee_page(self):
        self.page.goto("https://d.hr.dmerej.info/add_employee")

    def is_employee_in_employee_list(self, employee: Employee) -> bool:
        self.navigate_to_employee_list_page()

        employee_cell = self.page.get_by_role("cell", name=employee.basic_info.name, exact=True)
        return employee_cell.is_visible()

    def add_employee(self, employee: Employee):
        self.navigate_to_add_employee_page()

        self.page.get_by_placeholder("Name").click()
        self.page.get_by_placeholder("Name").fill(employee.basic_info.name)
        self.page.get_by_placeholder("Email").click()
        self.page.get_by_placeholder("Email").fill(employee.basic_info.email)
        self.page.get_by_role("button", name="Add").click()
        self.page.locator("#id_address_line1").click()
        self.page.locator("#id_address_line1").fill(employee.address.address_line1)
        if employee.address.address_line2:
            self.page.locator("#id_address_line2").click()
            self.page.locator("#id_address_line2").fill(employee.address.address_line2)
        self.page.get_by_placeholder("City").click()
        self.page.get_by_placeholder("City").fill(employee.address.city)
        self.page.get_by_placeholder("Zip code").click()
        self.page.get_by_placeholder("Zip code").fill(employee.address.zip_code)
        self.page.get_by_role("group", name="Contract").click()
        self.page.get_by_placeholder("Hiring date").fill(employee.contract.hiring_date)
        self.page.get_by_placeholder("Job title").click()
        self.page.get_by_placeholder("Job title").fill(employee.contract.job_title)
        self.page.get_by_role("button", name="Add").click()

    def navigate_to_edit_employee(self, employee: Employee):
        self.navigate_to_employee_list_page()
        self.page.get_by_role("link", name="Edit").click() # TODO: click on the right employee

    def edit_employee_address(self, employee: Employee, new_address: Address):
        self.navigate_to_edit_employee(employee)

        self.page.get_by_role("link", name="Update address").click()
        self.page.locator("#id_address_line1").click()
        self.page.locator("#id_address_line1").fill(new_address.address_line1)

        if new_address.address_line2:
            self.page.locator("#id_address_line2").click()
            self.page.locator("#id_address_line2").fill(new_address.address_line2)

        self.page.locator("#id_city").click()
        self.page.locator("#id_city").fill(new_address.city)

        self.page.locator("#id_zip_code").click()
        self.page.locator("#id_zip_code").fill(new_address.zip_code)

        self.page.get_by_role("button", name="Update").click()


    def saved_address_on_page(self, employee: Employee) -> Address:
        self.navigate_to_edit_employee(employee)
        self.page.get_by_role("link", name="Update address").click()
        return Address(
            address_line1=self.page.locator("#id_address_line1").get_attribute("value") or "",
            address_line2=self.page.locator("#id_address_line2").get_attribute("value") or "",
            city=self.page.locator("#id_city").get_attribute("value") or "",
            zip_code=self.page.locator("#id_zip_code").get_attribute("value") or "",
        )
    
    def add_employee_to_team(self, employee: Employee, team: Team):
        self.navigate_to_edit_employee(employee)

        self.page.get_by_role("link", name="Add to team").click()
        self.page.get_by_label("Team").select_option(index=1)  # TODO: replace with team name 
        self.page.get_by_role("button", name="Add").click()
        

        

