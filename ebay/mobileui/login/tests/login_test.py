import unittest
from ebay.mobileui.login.action.login_page import UserLogin

user_name = 'dasajitkumar@gmail.com'
password = '123abc?'
short_name = 'ajit'


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user_login = UserLogin()

    def test_login(self):
        assert self.user_login.login(user_name, password, short_name), "login test is not successful"

    def test_check_already_login(self):
        self.user_login.check_already_login(short_name)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()