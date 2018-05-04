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

        :param locator:
        :param wait_time:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator))
            element.click()
            self.wait_for_loading()
        except Exception as e:
            self.log.info("Exception while clicking the element " + str(e))

    def send_keys(self, locator, key_inputs):
        """
        Typing keys at input locator
        :param locator:
        :param key_inputs:
        """
        try:
            WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(locator)).send_keys(key_inputs)
        except Exception as e:
            self.log.info("Exception while sending keys :" + str(e))

    def find_element(self, locator):
        """

        :param locator:
        :return:
        """
        try:
            element = self.driver.find_element(*locator)
            return element
        except Exception as e:
            self.log.info("Exception while finding the element " + str(e))

    def wait_for_element(self, locator):
        """

        :param locator:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            self.log.info("Exception while waiting for the element " + str(e))

    def wait_for_loading(self):
        """

        :return:
        """
        try:
            WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(
                EC.invisibility_of_element_located(self.progress_bar))
        except Exception as e:
            self.log.info("Exception while waiting for the progress bar to disappear " + str(e))

