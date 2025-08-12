import pytest
import re
from playwright.sync_api import Page, expect
from pages.playwright_homepage import PlaywrightHomepage


@pytest.fixture
def homepage(page: Page):
    homepage = PlaywrightHomepage(page)
    return homepage

def test_homepage_loaded(homepage, page):
    homepage.navigate_to_homepage()
    expect(page).to_have_title(re.compile("Playwright"))
    expect(homepage.logo).to_be_visible()
    expect(homepage.description).to_be_visible()

# Happy path
def test_search_functionality(homepage, page):
    homepage.navigate_to_homepage()
    expect(homepage.logo).to_be_visible()
    homepage.search.click()
    homepage.validate_search_functionality("page object model")
    expect(page).to_have_url("https://playwright.dev/docs/pom")

