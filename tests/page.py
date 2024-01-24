from playwright.sync_api import sync_playwright

from .database import reset_database

def with_playwright_page(func):
    def wrapper(*args, **kwargs):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            reset_database(page)

            func(page, *args, **kwargs)

            context.close()
            browser.close()

    return wrapper


