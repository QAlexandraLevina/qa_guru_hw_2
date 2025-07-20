import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_height = 900
    browser.config.window_width = 1600
    browser.open('https://duckduckgo.com')

    yield

    browser.quit()