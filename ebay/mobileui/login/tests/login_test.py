import yaml
import unittest
from ebay.mobileui.login.action.login_page import UserLogin


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user_login = UserLogin()
        test_data = yaml.load(open('purchase_flow.yaml', 'r'))
        self.user_name = test_data['UNIT_TEST']['login_user']
        self.password = test_data['UNIT_TEST']['password']
        self.short_name = test_data['UNIT_TEST']['short_name']

    def test_login(self):
        assert self.user_login.login(self.user_name, self.password, self.short_name), "login test is not successful"

    def test_check_already_login(self):
        self.user_login.check_already_login(self.short_name)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()