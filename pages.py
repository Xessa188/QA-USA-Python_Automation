from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import card_number


class UrbanRoutesPage:
    FROM_FIELD = By.ID, 'from'
    TO_FIELD = By.ID, 'to'
    CALL_A_TAXI_BUTTON = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_PLAN_BUTTON = (By.XPATH, "//div[text()='Supportive']")
    PHONE_NUMBER_OPTION = (By.XPATH, "//div[text()='Phone number']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@id='phone']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    CODE_FIELD = (By.XPATH, "//input[@id='code']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    PAYMENT_METHOD = (By.XPATH, "//div[@class='pp-button filled' and .//div[text()='Payment method']]")
    CLOSE_PAYMENT_METHOD = (
        By.XPATH,
        "//div[contains(@class,'payment-picker') and contains(@class,'open')]//button[contains(@class,'section-close')]"
    )
    ADD_CARD = (By.XPATH, "//img[@class='pp-plus' and @alt='plus']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@id='number']")
    CARD_CODE_FIELD = ( By.XPATH, "//input[@id='code' and @class='card-input' and @placeholder='12']" )
    LINK_CARD_BUTTON = (By.XPATH, "//button[text()='Link']")
    MESSAGE_TO_DRIVER_FIELD = (By.XPATH, "//input[@id='comment']")
    BLANKETS_AND_HANDKERCHIEFS_SLIDER = (
        By.XPATH,
        "//div[@class='r-sw-label' and text()='Blanket and handkerchiefs']/following-sibling::div//div[@class='switch']")

    BLANKETS_AND_HANDKERCHIEFS_CHECKBOX = (
        By.XPATH,
        "//div[@class='r-sw-label' and text()='Blanket and handkerchiefs']/following-sibling::div//input[@class='switch-input']")

    ORDER_2_ICE_CREAMS = (By.XPATH, "//div[@class='counter-plus']")
    ICE_CREAM_COUNT = (By.XPATH, "//div[@class='counter-value']")
    CLICK_ORDER_BUTTON = (By.CSS_SELECTOR, "button.smart-button")
    CAR_SEARCH_MODAL = (By.XPATH, "//div[@class='order-body']")

    def __init__(self, driver):
        self.driver = driver

    def input_from_address(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def input_to_address(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to_address(self):
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def click_call_a_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CALL_A_TAXI_BUTTON)
        ).click()

    def click_supportive_plan_button(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_BUTTON).click()

    def get_supportive_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_BUTTON).text

    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_OPTION).click()

    def write_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD).get_property('value')

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def write_code(self, code):
        self.driver.find_element(*self.CODE_FIELD).send_keys(code)

    def get_code(self):
        self.driver.find_element(*self.CODE_FIELD).get_property('value')

    def click_confirm(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def click_payment_method(self):
            self.driver.find_element(*self.PAYMENT_METHOD).click()

    def close_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE_PAYMENT_METHOD)
        ).click()

    def add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def card_number_field(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_number)

    def get_card_number(self):
         return self.driver.find_element(*self.CARD_NUMBER_FIELD).get_property('value')

    def card_code_field(self, card_code):
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.CARD_CODE_FIELD).get_property('value')

    def link_card_button(self):
        self.driver.find_element(*self.LINK_CARD_BUTTON).click()

    def message_to_driver_field(self, message_for_driver_field):
        self.driver.find_element(*self.MESSAGE_TO_DRIVER_FIELD).send_keys(message_for_driver_field)

    def get_message_to_driver_field(self):
        return self.driver.find_element(*self.MESSAGE_TO_DRIVER_FIELD).get_property('value')

    def blankets_and_handkerchiefs_slider(self):
        checkbox = self.driver.find_element(*self.BLANKETS_AND_HANDKERCHIEFS_CHECKBOX
        )
        self.driver.execute_script("arguments[0].click();", checkbox)

    def is_blankets_and_handkerchiefs_slider(self):
        return self.driver.find_element(*self.BLANKETS_AND_HANDKERCHIEFS_CHECKBOX).get_property('checked')

    def order_2_ice_creams(self):
        for _ in range(2):
            plus_button = self.driver.find_element(*self.ORDER_2_ICE_CREAMS)
            self.driver.execute_script("arguments[0].click();", plus_button)

    def ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT).text

    def click_order_button(self):
        self.driver.find_element(*self.CLICK_ORDER_BUTTON).click()

    def car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()

