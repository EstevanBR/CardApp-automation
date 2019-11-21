from __future__ import annotations
from page.page import Page, TextCallback
from xcui_element.xcui_element_types import XCUIElementType
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webelement import WebElement


class CardPage(Page):
    @property
    def _view(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.view"))

    @property
    def _questionLabel(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.questionLabel"))

    @property
    def _currentCardLabel(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.currentCardLabel"))

    @property
    def _completedLabel(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.completedLabel"))

    @property
    def _prevCardButton(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.prevCardButton"))

    @property
    def _nextCardButton(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.nextCardButton"))

    @property
    def _completeCardButton(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.completeCardButton"))

    @property
    def _recordButton(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.recordButton"))

    @property
    def _playButton(self) -> WebElement:
        return Page.find_element((MobileBy.ACCESSIBILITY_ID, "CardView.playButton"))

    def __init__(self):
        assert self._view.is_displayed()

    def tap_record_button(self) -> CardPage:
        self._recordButton.click()
        return CardPage()

    def tap_complete_card_button(self) -> CardPage:
        self._completeCardButton.click()
        return CardPage()

    def get_record_button_text(self) -> CardPage:
        self._recordButton.text()
        return CardPage()

    def tap_play_button(self) -> PlaybackAlertPage:
        from pages.playback_alert_page import PlaybackAlertPage
        self._playButton.click()
        return PlaybackAlertPage()

    def get_play_button_text(self) -> CardPage:
        self._playButton.text()
        return CardPage()

    def dismiss_via_swipe(self) -> QuestionsPage:
        from pages.questions_page import QuestionsPage

        self._swipe_down()
        return QuestionsPage()

    def get_question_text(self, text_callback: TextCallback) -> CardPage:
        text_callback(self._questionLabel.text)
        return CardPage()
