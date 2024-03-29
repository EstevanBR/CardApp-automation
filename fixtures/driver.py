import pytest
import socket
import logging
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver import Proxy


@pytest.fixture(scope="module", autouse=False)
def driver(mock, desired_capabilities: dict) -> WebDriver:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    driver = WebDriver(
        command_executor=f"http://{ip}:4723/wd/hub",
        desired_capabilities=desired_capabilities,
        direct_connection=True,
        keep_alive=True
    )
    driver.implicitly_wait(3)
    logging.debug(
        f"created driver with desired_capabilities: {desired_capabilities}")

    return driver


@pytest.fixture(scope="module", autouse=False)
def driver_setup(driver: WebDriver) -> None:
    logging.debug(f"starting driver session")

    driver.terminate_app(driver.desired_capabilities["bundleId"])
    driver.execute_script(
        "mobile: launchApp",
        {
            "bundleId": driver.desired_capabilities["bundleId"],
            "arguments": driver.desired_capabilities["processArguments"]["args"]
        }
    )
    driver.execute_script(
        "mobile: activateApp",
        {
            "bundleId": driver.desired_capabilities["bundleId"]
        }
    )


@pytest.fixture(scope="module", autouse=False)
def driver_teardown(driver: WebDriver) -> None:
    yield None
    logging.debug(f"ending driver session")
    driver.quit()
