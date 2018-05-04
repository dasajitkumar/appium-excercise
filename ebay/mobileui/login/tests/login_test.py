import unittest
from ebay.mobileui.login.action.login_page import UserLogin

ip_address = '127.0.0.1'
port_no = '4723'
desire_capabilities = {
                      "platformName": "Android",
                      "platformVersion": "5.1",
                      "deviceName": "HYFALBV899999999",
                      "appPackage": "com.ebay.mobile",
                      "appActivity": "com.ebay.mobile.activities.MainActivity"
                    }
user_name = 'dasajitkumar@gmail.com'
password = '123abc?'
short_name = 'ajit'


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user_login = UserLogin(ip_address, port_no, desire_capabilities)

    def test_login(self):
        assert self.user_login.login(user_name, password, short_name), "login test is not successful"

    def test_check_already_login(self):
        self.user_login.check_already_login(short_name)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()