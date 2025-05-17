from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code


class RouteAutomationPage:
    origin_input = (By.ID, 'from')
    destination_input = (By.ID, 'to')

    plan_support_card = (By.XPATH, '//div[contains(text(), "Suporte")]')
    plan_card_container = (By.XPATH, '//div[contains(text(), "Suporte")]//..')
    selected_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    start_ride_button = (By.XPATH, '//button[contains(text(), "Chamar um táxi")]')

    phone_button = (By.CLASS_NAME, "np-button")
    input_phone_number = (By.ID, 'phone')
    input_sms_code = (By.ID, 'code')
    next_step_button = (By.CSS_SELECTOR, '.full')
    confirm_sms_button = (By.XPATH, '//button[contains(text(), "Confirmar")]')
    phone_display = (By.ID, 'phone')

    open_payment_options = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Método de pagamento")]')
    add_card_button = (By.XPATH, '//div[contains(text(), "Adicionar cartão")]')
    field_card_number = (By.ID, 'number')
    field_card_code = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    link_card_button = (By.XPATH, '//button[contains(text(), "Link")]')
    close_payment_modal = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    current_payment_label = (By.CLASS_NAME, 'pp-value-text')

    driver_notes_field = (By.ID, 'comment')
    toggle_elements = (By.CLASS_NAME, 'switch')
    toggle_checkboxes = (By.CLASS_NAME, 'switch-input')
    increase_item_button = (By.CLASS_NAME, 'counter-plus')
    item_quantity_display = (By.CLASS_NAME, 'counter-value')

    submit_order_button = (By.CLASS_NAME, 'button')
    order_confirmation_box = (By.CLASS_NAME, 'reqs')

    def __init__(self, driver):
        self.driver = driver

    def insert_origin(self, origin):
        field = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.origin_input))
        field.send_keys(origin)

    def insert_destination(self, destination):
        self.driver.find_element(*self.destination_input).send_keys(destination)

    def get_origin_value(self):
        return self.driver.find_element(*self.origin_input).get_property('value')

    def get_destination_value(self):
        return self.driver.find_element(*self.destination_input).get_property('value')

    def click_start_ride(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.start_ride_button))
        self.driver.find_element(*self.start_ride_button).click()

    def define_route(self, origin, destination):
        self.insert_origin(origin)
        self.insert_destination(destination)
        self.click_start_ride()

    def choose_support_plan(self):
        if self.driver.find_element(*self.plan_card_container).get_attribute("class") != "tcard active":
            plan = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.plan_support_card))
            self.driver.execute_script("arguments[0].scrollIntoView();", plan)
            plan.click()

    def get_selected_plan(self):
        return self.driver.find_element(*self.selected_plan_card).text

    def register_phone(self, phone):
        self.driver.find_element(*self.phone_button).click()
        self.driver.find_element(*self.input_phone_number).send_keys(phone)
        self.driver.find_element(*self.next_step_button).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.input_sms_code).send_keys(code)
        self.driver.find_element(*self.confirm_sms_button).click()

    def fetch_phone(self):
        return self.driver.find_element(*self.phone_display).get_property('value')

    def fill_card_details(self, number, code):
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "overlay")))
        self.driver.find_element(*self.open_payment_options).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.field_card_number).send_keys(number)
        self.driver.find_element(*self.field_card_code).send_keys(code)
        self.driver.find_element(*self.link_card_button).click()
        self.driver.find_element(*self.close_payment_modal).click()

    def read_payment_method(self):
        return self.driver.find_element(*self.current_payment_label).text

    def write_driver_message(self, note):
        self.driver.find_element(*self.driver_notes_field).send_keys(note)

    def read_driver_message(self):
        return self.driver.find_element(*self.driver_notes_field).get_property('value')

    def toggle_blanket_option(self):
        self.driver.find_elements(*self.toggle_elements)[0].click()

    def is_blanket_option_checked(self):
        return self.driver.find_elements(*self.toggle_checkboxes)[0].get_property('checked')

    def add_ice_creams(self, quantity: int):
        buttons = self.driver.find_elements(*self.increase_item_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", buttons[0])
        for _ in range(quantity):
            buttons[0].click()

    def read_ice_cream_count(self):
        return int(self.driver.find_elements(*self.item_quantity_display)[0].text)

    def place_order(self):
        self.driver.find_element(*self.submit_order_button).click()

    def is_order_confirmed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.order_confirmation_box))
        return self.driver.find_element(*self.order_confirmation_box).is_displayed()
