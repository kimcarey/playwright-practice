import re

from playwright.sync_api import Page, expect


class PlaywrightHomepage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://playwright.dev/"
        self.logo = page.get_by_role("img", name="Playwright logo")
        self.heading = page.get_by_role("heading", name=re.compile("Playwright"))
        self.description = page.get_by_text(" enables reliable end-to-end testing for modern web apps")
        self.search = page.locator("button", has_text="Search")
        self.search_input_box = page.get_by_placeholder("Search docs")

    def navigate_to_homepage(self):
        self.page.goto(self.url)

    def validate_search_functionality(self, query: str):
        self.search_for(query)

    def search_for(self, query: str):
        self.search_input_box.fill(query)
        # playwright.dev provides autocomplete search results as you type
        # Approach: Wait for search suggestions to appear
        first_suggestion = self.page.locator(".DocSearch-Hit").first
        expect(first_suggestion).to_be_visible(timeout=3000)
        # Click the first suggestion
        first_suggestion.click()