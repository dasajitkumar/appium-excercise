from ebay.mobileui.utils.base_page import BasePage
from selenium.webdriver.common.by import By


class UserLogin:
    # Login Locators
    login_button = (By.ID, 'com.ebay.mobile:id/button_sign_in')
    user_name = (By.ID, 'com.ebay.mobile:id/edit_text_username')
    password = (By.ID, 'com.ebay.mobile:id/edit_text_password')
    sign_in_button = (By.ID, 'com.ebay.mobile:id/button_sign_in')
    no_thanks_opt = (By.ID, 'com.ebay.mobile:id/button_google_deny')

    # Check Already Login Locators
    side_bar = (By.ID, 'com.ebay.mobile:id/home')
    user_bar = (By.XPATH, '//android.widget.LinearLayout[@content-desc="Featured Deals,3 items"]/android.widget.LinearLayout/android.widget.LinearLayout')

    def __init__(self, ip_address, port_no, desire_capabilities):
        self.base_page = BasePage(ip_address, port_no, desire_capabilities)
        self.log = self.base_page.log

    def login(self, user, pass_word, short_name, submit=True):
        """
        Login into ebay mobile ui
        :param user_name: ebay user name
        :param password: ebay password
        :param submit: Default True and it also accepts False
        :return: true
        """
        if not self.check_already_login(short_name):
            self.base_page.click(self.login_button)
            self.base_page.send_keys(self.user_name, user)
            self.base_page.send_keys(self.password, pass_word)
            if submit:
                self.base_page.click(self.sign_in_button)
                self.base_page.click(self.no_thanks_opt)
                if self.check_already_login(short_name):
                    return True
                else:
                    return False
        else:
            self.base_page.log.info("Already logged in...")

    def check_already_login(self, user_name):
        login_status = False
        self.base_page.click(self.side_bar)
        user_bar_element = self.base_page.wait_for_element(self.user_bar)
        if user_name in user_bar_element.text:
            login_status = True
        self.base_page.click(self.side_bar)
        return login_status


