from __future__ import annotations

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webelement import WebElement

from page.page import Page as Page

from xcui_element.xcui_element_types import XCUIElementType


class PlaybackAlertPage(Page):
    @property
    def _sheet(self) -> WebElement:
        return Page.find_element((MobileBy.CLASS_NAME, XCUIElementType.Sheet))

    @property
    def _title(self) -> WebElement:
        return self._sheet.find_element_by_name("Audio Output")

    def __init__(self):
        assert self._title.is_displayed()

    def tap_default_button(self) -> CardPage:
        from pages.card_page import CardPage

        self._sheet.find_element_by_name("Default").click()
        return CardPage()

    def tap_speaker_button(self) -> CardPage:
        from pages.card_page import CardPage

        self._sheet.find_element_by_name("Speaker").click()
        return CardPage()
