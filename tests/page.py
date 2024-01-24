from playwright.sync_api import sync_playwright


def with_playwright_page(func):
    def wrapper(*args, **kwargs):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            func(page, *args, **kwargs)

            context.close()
            browser.close()

    return wrapper


