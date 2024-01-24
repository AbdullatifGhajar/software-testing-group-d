from playwright.sync_api import Page

from .team import Team, TeamPage
from .employee import Employee, EmployeePage, BasicInfo, Address, Contract


def test_add_team(reset_db, page: Page):
    team = Team(name="Team A")
    team_page = TeamPage(page)

    team_page.add_team(team)
    assert team_page.is_team_in_team_list(team)

def test_delete_team(reset_db, page: Page):
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
    team = Team(name="Team A")

    team_page = TeamPage(page)
    employee_page = EmployeePage(page)

    team_page.add_team(team)
    employee_page.add_employee(employee)

    # employee is there
    assert employee_page.is_employee_in_employee_list(employee)

    employee_page.add_employee_to_team(employee, team)
    team_page.delete_team(team)

    # employee should stay there
    assert employee_page.is_employee_in_employee_list(employee)