import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ebay.mobileui.utils.driver_init import RemoteInit

DEFAULT_WAIT_TIME = 10


class BasePage:
    progress_bar = (By.ID, 'progress_bar')

    def __init__(self):
        """
        Initializing the appium driver
        :param driver: appium device driver
        """
        remote_inst = RemoteInit()
        self.driver = remote_inst.driver
        logging.getLogger().setLevel(logging.INFO)
        self.log = logging.getLogger(__name__)

    def click(self, locator, wait_time=DEFAULT_WAIT_TIME):
        """
        Wrapper for the appium click api
        :param locator: appium location
        :param wait_time: wait time till item to be click able
        :return: element/None
        """
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator))
            element.click()
            self.wait_for_loading()
        except Exception as e:
            self.log.info("Exception while clicking the element " + str(e))

    def send_keys(self, locator, key_inputs):
        """
        Wrapper for the send_keys appium api
        :param locator: appium locator
        :param key_inputs: text to be typed
        """
        try:
            WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(locator)).send_keys(key_inputs)
        except Exception as e:
            self.log.info("Exception while sending keys :" + str(e))

    def find_element(self, locator):
        """
        Wrapper for the find_element appium API
        :param locator: appuim locator
        :return: element/None
        """
        try:
            element = self.driver.find_element(*locator)
            return element
        except Exception as e:
            self.log.info("Exception while finding the element " + str(e))

    def wait_for_element(self, locator, wait_time=DEFAULT_WAIT_TIME):
        """
        Wait till element to be located
        :param locator: appium locator
        :return: element/None
        """
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            self.log.info("Exception while waiting for the element " + str(e))

    def wait_for_loading(self):
        """
        Wait till progress bar to be disappeared
        :return: None
        """
        try:
            WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(
                EC.invisibility_of_element_located(self.progress_bar))
        except Exception as e:
            self.log.info("Exception while waiting for the progress bar to disappear " + str(e))

