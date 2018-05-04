from selenium.webdriver.common.by import By
from ebay.mobileui.search.action.product_search_page import ProductSearch


class PurchasePoduct(ProductSearch):
    buy_it_now = (By.ID, 'button_bin')
    category_selection = (By.ID, 'spinner_selection_option')
    category_option = (By.XPATH, '//android.widget.ListView/android.widget.FrameLayout[2]')
    buy_it_now_after = (By.ID, 'button_bin_buybar')

    def purchase_product(self, product_name=False):
        """

        :return:
        """
        if product_name:
            self.base_page.click(self.home_search_bar)
            self.base_page.send_keys(self.search_bar_after_click, product_name)
            self.base_page.click(self.suggest_list)
            self.base_page.click(self.pop_up)
            self.base_page.click(self.first_search_result)
        self.base_page.click(self.buy_it_now)
        self.base_page.click(self.category_selection)
        self.base_page.click(self.category_option)
        self.base_page.click(self.buy_it_now_after)