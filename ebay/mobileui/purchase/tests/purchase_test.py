import yaml
import unittest
from ebay.mobileui.login.action.login_page import UserLogin
from ebay.mobileui.purchase.action.purchase_page import PurchasePoduct

user_name = 'dasajitkumar@gmail.com'
password = '123abc?'
short_name = 'ajit'


class ProductSearchTest(unittest.TestCase):
    def setUp(self):
        self.user_login = UserLogin()
        self.product_purchase = PurchasePoduct(self.user_login.base_page)
        test_data = yaml.load(open('purchase_flow.yaml', 'r'))
        self.user_name = test_data['UNIT_TEST']['login_user']
        self.password = test_data['UNIT_TEST']['password']
        self.short_name = test_data['UNIT_TEST']['short_name']
        self.product_name = test_data['UNIT_TEST']['product_name']
        self.user_login.login(self.user_name, self.password, self.short_name)

    def test_search_product(self):
        self.product_purchase.purchase_product(self.product_name)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()