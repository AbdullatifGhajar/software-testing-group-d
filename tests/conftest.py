import pytest

from playwright.sync_api import Page


@pytest.fixture
def reset_db(page: Page):
    page.goto("https://d.hr.dmerej.info/")
    page.get_by_role("link", name="Reset database").click()
    page.get_by_role("button", name="Proceed").click()
