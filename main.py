import data
import helpers
from selenium import webdriver
from pages import RouteAutomationPage


class UrbanRoutesTestSuite:
    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.BASE_URL)
        cls.driver.set_window_size(1280, 720)
        cls.page = RouteAutomationPage(cls.driver)

    def test_define_route(self):
        self.page.define_route(data.ORIGIN_ADDRESS, data.DESTINATION_ADDRESS)
        assert self.page.get_origin_value() == data.ORIGIN_ADDRESS
        assert self.page.get_destination_value() == data.DESTINATION_ADDRESS

    def test_choose_support_plan(self):
        self.page.choose_support_plan()
        assert self.page.get_selected_plan() == "Work"

    def test_register_phone(self):
        self.page.register_phone(data.USER_PHONE)
        assert self.page.fetch_phone() == data.USER_PHONE

    def test_fill_card_details(self):
        self.page.fill_card_details(data.CREDIT_CARD, data.SECURITY_CODE)
        assert self.page.read_payment_method() == "Cartão"

    def test_write_driver_note(self):
        self.page.write_driver_message(data.DRIVER_NOTE)
        assert self.page.read_driver_message() == data.DRIVER_NOTE

    def test_toggle_blanket(self):
        self.page.toggle_blanket_option()
        assert self.page.is_blanket_option_checked() is True

    def test_add_ice_creams(self):
        self.page.add_ice_creams(data.DESSERT_QUANTITY)
        assert self.page.read_ice_cream_count() == data.DESSERT_QUANTITY

    def test_place_order(self):
        self.page.place_order()
        assert self.page.is_order_confirmed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
