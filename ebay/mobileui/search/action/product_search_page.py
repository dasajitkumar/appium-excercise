from selenium.webdriver.common.by import By


class ProductSearch:
    home_search_bar = (By.ID, 'search_box')
    search_bar_after_click = (By.ID, 'search_src_text')
    suggest_list = (By.XPATH, '//android.widget.ListView/android.widget.RelativeLayout[1]')
    pop_up = (By.ID, 'popup_container')
    first_search_result = (By.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]")
    buy_it_now = (By.ID, 'button_bin')
    category_selection = (By.ID, 'spinner_selection_option')
    category_option = (By.XPATH, '//android.widget.ListView/android.widget.FrameLayout[2]')
    buy_it_now_after = (By.ID, 'button_bin_buybar')

    def __init__(self, base_page):
        self.base_page = base_page

    def search_product(self, prod_name, open_product=False):
        """
        Search a product and open the search result
        :param prod_name: product name
        :param open_product: first_item (to open the first search result)
        :return: None
        """
        self.base_page.click(self.home_search_bar)
        self.base_page.send_keys(self.search_bar_after_click, prod_name)
        self.base_page.click(self.suggest_list)
        self.base_page.click(self.pop_up)
        if open_product and open_product.lower() == 'first_item':
            self.base_page.click(self.first_search_result)

