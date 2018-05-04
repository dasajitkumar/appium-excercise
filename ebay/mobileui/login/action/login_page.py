from ebay.mobileui.utils.base_page import BasePage
from selenium.webdriver.common.by import By


class UserLogin:
    # Login Locators
    login_button = (By.ID, 'button_sign_in')
    user_name = (By.ID, 'edit_text_username')
    password = (By.ID, 'edit_text_password')
    sign_in_button = (By.ID, 'button_sign_in')
    no_thanks_opt = (By.ID, 'button_google_deny')

    # Check Already Login Locators
    side_bar_open = (By.ID, 'home')
    side_bar_close = (By.ID, 'menuitem_home')
    user_sign_in = (By.ID, 'textview_sign_in_status')
    user_sign_out = (By.ID, 'textview_sign_out_status')

    def __init__(self):
        self.base_page = BasePage()
        self.log = self.base_page.log

    def login(self, user, pass_word, short_name, submit=True):
        """
        Login into ebay mobile ui
        :param user: ebay user name
        :param pass_word: ebay password
        :param short_name: short name of the user
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
        """

        :param user_name:
        :return:
        """
        login_status = False
        self.base_page.click(self.side_bar_open)
        user_sign_out_status = self.base_page.wait_for_element(self.user_sign_out)
        if not user_sign_out_status:
            user_sign_in_satus = self.base_page.wait_for_element(self.user_sign_in)
            if user_name in user_sign_in_satus.text:
                login_status = True
        self.base_page.click(self.side_bar_close)
        return login_status


