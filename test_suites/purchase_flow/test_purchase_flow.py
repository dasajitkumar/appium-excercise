import yaml
import unittest
from ebay.mobileui.login.action.login_page import UserLogin
from ebay.mobileui.purchase.action.purchase_page import PurchasePoduct


class TestPurchaseFlow(unittest.TestCase):
    def setUp(self):
        user_login = UserLogin()
        self.product_purchase = PurchasePoduct(user_login.base_page)
        test_data = yaml.load(open('purchase_flow.yaml', 'r'))
        self.user_name = test_data['TEST_PURCHASE_FLOW']['login_user']
        self.password = test_data['TEST_PURCHASE_FLOW']['password']
        self.short_name = test_data['TEST_PURCHASE_FLOW']['short_name']
        self.product_name= test_data['TEST_PURCHASE_FLOW']['product_name']
        user_login = UserLogin()
        self.product_purchase = PurchasePoduct(user_login.base_page)
        user_login.login(self.user_name, self.password, self.short_name)

    def test_purchase(self):
        self.product_purchase.purchase_product(self.product_name)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

