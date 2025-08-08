from playwright.sync_api import Page, expect


class DuckDuckGoHomepage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box_locator = page.get_by_placeholder("Search without being tracked")

    def navigate_to_homepage(self):
        self.page.goto("https://duckduckgo.com/")

    def validate_search_box(self):
        expect(self.search_box_locator).to_be_visible()