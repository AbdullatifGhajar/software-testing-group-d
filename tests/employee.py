from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class Employee:
    name: str
    email: str
    address_line1: str
    address_line2: str
    city: str
    zip_code: str
    hiring_date: str
    job_title: str


def add_employee(page: Page, employee: Employee) -> None:
    page.goto("https://d.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(employee.name)
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(employee.email)
    page.get_by_role("button", name="Add").click()
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill(employee.address_line1)
    if employee.address_line2:
        page.locator("#id_address_line2").click()
        page.locator("#id_address_line2").fill(employee.address_line2)
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill(employee.city)
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill(employee.zip_code)
    page.get_by_role("group", name="Contract").click()
    page.get_by_placeholder("Hiring date").fill(employee.hiring_date)
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill(employee.job_title)
    page.get_by_role("button", name="Add").click()
