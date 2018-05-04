import unittest
from ebay.mobileui.login.action.login_page import UserLogin
from ebay.mobileui.search.action.product_search_page import ProductSearch

user_name = 'dasajitkumar@gmail.com'
password = '123abc?'
short_name = 'ajit'


class ProductSearchTest(unittest.TestCase):
    def setUp(self):
        self.user_login = UserLogin()
        self.product_search = ProductSearch(self.user_login.base_page)
        self.user_login.login(user_name, password, short_name)

    def test_search_product(self):
        self.product_search.search_product('iphonex', 'first_item')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
