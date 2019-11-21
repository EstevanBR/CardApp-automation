from __future__ import annotations

import time
from typing import Tuple, Callable

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

TextCallback = Callable[[str], None]
Strategy = Tuple[MobileBy, str]


class Page:
    """Base class for PageObjects.

    Attributes:
        _driver: Webdriver
    """
    _driver: WebDriver

    @classmethod
    def inject_driver(cls, driver: WebDriver):
        Page._driver = driver

    @classmethod
    def find_element(cls, strategy: Strategy) -> WebElement:
        return Page._driver.find_element(*strategy)

    def sleep(self, duration: float):
        time.sleep(duration)
        return self

    def _swipe_down(self):
        Page._driver.execute_script("mobile: swipe", {"direction": "down"})

    def _swipe_up(self):
        Page._driver.execute_script("mobile: swipe", {"direction": "up"})

    def _swipe_left(self):
        Page._driver.execute_script("mobile: swipe", {"direction": "left"})

    def _swipe_right(self):
        Page._driver.execute_script("mobile: swipe", {"direction": "right"})
