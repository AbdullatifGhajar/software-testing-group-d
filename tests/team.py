from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class Team:
    name: str
    employees: list

    def __init__(self, name: str, employees: list | None = None):
        self.name = name
        self.employees = employees or []


class TeamPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_team_list_page(self):
        self.page.goto("https://d.hr.dmerej.info/teams")

    def navigate_to_add_team_page(self):
        self.page.goto("https://d.hr.dmerej.info/add_team")

    def is_team_in_team_list(self, team: Team) -> bool:
        self.navigate_to_team_list_page()

        team_cell = self.page.get_by_role("cell", name=team.name, exact=True)
        return team_cell.is_visible()
    
    def add_team(self, team: Team):
        self.navigate_to_add_team_page()

        self.page.get_by_placeholder('Name').click()
        self.page.get_by_placeholder('Name').fill(team.name)
        self.page.get_by_role("button", name="Add").click()

    def delete_team(self, team: Team):
        self.navigate_to_team_list_page()
        # TODO: delete the correct team

        self.page.get_by_role("link", name="Delete").click()
        self.page.get_by_role("button", name="Proceed").click()
