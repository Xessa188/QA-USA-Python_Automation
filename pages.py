from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class UrbanRoutesPage:
    #
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_A_TAXI_MAIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button round')]")

    SUPPORTIVE_TARIFF_BUTTON = (By.XPATH, "//button[@data-for='tariff-card-4']")
    SUPPORTIVE_TARIFF_CARD_ACTIVE = (By.XPATH, "//div[contains(@class, 't_supportive') and contains(@class, 'active')]")

    PHONE_BUTTON = (By.CLASS_NAME, 'np-button')
    PHONE_INPUT_FIELD = (By.XPATH, "//input[@id='phone']")
    PHONE_NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    SMS_CODE_FIELD = (By.ID, 'code')
    SMS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button')
    PAYMENT_METHOD_TEXT = (By.CLASS_NAME, 'pp-value_text')
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@id='number']")
    CARD_CVV_FIELD = (By.XPATH, "//div[@class='card-second-row']//input[@id='code']")

    PAYMENT_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'payment-picker') and contains(@class, 'open')]")
    CLOSE_PAYMENT_MODAL = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    COMMENT_FIELD = (By.ID, 'comment')
    BLANKET_TOGGLE_SWITCH = (By.XPATH,
                             "//div[text()='Blanket and handkerchiefs']/following-sibling::div//span[@class='slider round']")
    BLANKET_CHECKBOX_STATUS = (By.XPATH,
                               "//div[text()='Blanket and handkerchiefs']/following-sibling::div//input[@class='switch-input']")

    ICE_CREAM_PLUS_BUTTON = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-plus']")
    ICE_CREAM_COUNTER_VALUE = (By.XPATH,
                               "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-value']")

    ORDER_TAXI_BUTTON = (By.CLASS_NAME, 'smart-button')
    CAR_SEARCH_MODAL = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FROM_LOCATOR))
        field.send_keys(from_text)
        field.send_keys(Keys.ENTER)

    def enter_to_location(self, to_text):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TO_LOCATOR))
        field.send_keys(to_text)
        field.send_keys(Keys.ENTER)

    def get_from_value(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FROM_LOCATOR)).get_attribute(
            'value')

    def get_to_value(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TO_LOCATOR)).get_attribute(
            'value')

    def click_call_a_taxi_main_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CALL_A_TAXI_MAIN_BUTTON)).click()

    def select_supportive_tariff(self):
        # 🎯 Crucial Sync: Wait 1 second for the sliding panel layout animation to settle completely!
        time.sleep(1)

        tariff_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUPPORTIVE_TARIFF_BUTTON)
        )
        tariff_btn.click()
        time.sleep(1)

    def click_phone_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PHONE_BUTTON)).click()

    def fill_phone_number(self, phone_number):
        phone_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PHONE_INPUT_FIELD))
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def get_phone_field_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PHONE_INPUT_FIELD)).get_attribute('value')

    def click_phone_next(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PHONE_NEXT_BUTTON)).click()

    def enter_sms_code(self, sms_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SMS_CODE_FIELD)).send_keys(sms_code)

    def click_sms_confirm(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SMS_CONFIRM_BUTTON)).click()

    def click_payment_method(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)).click()

    def is_payment_modal_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PAYMENT_MODAL_WINDOW)).is_displayed()

    def click_add_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()

    def fill_card_details(self, card_num, cvv_code):
        card_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CARD_NUMBER_FIELD))
        card_field.send_keys(card_num)
        cvv_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CARD_CVV_FIELD))
        cvv_field.send_keys(cvv_code)
        cvv_field.send_keys(Keys.TAB)

    def is_link_button_clickable(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Link']"))).is_enabled()

    def click_link_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Link']"))).click()

    def close_payment_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLOSE_PAYMENT_MODAL)).click()

    def get_payment_method_text(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PAYMENT_METHOD_TEXT)).text

    def enter_driver_comment(self, comment_text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COMMENT_FIELD)).send_keys(
            comment_text)

    def get_driver_comment_value(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COMMENT_FIELD)).get_attribute(
            'value')

    def toggle_blanket_option(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BLANKET_TOGGLE_SWITCH)).click()

    def is_blanket_property_checked(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BLANKET_CHECKBOX_STATUS)).get_property('checked')

    def order_ice_creams(self, count):
        plus_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS_BUTTON))
        for _ in range(count):
            plus_btn.click()

    def get_ice_cream_count(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ICE_CREAM_COUNTER_VALUE)).text

    def click_order_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_TAXI_BUTTON)).click()

    def is_car_search_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAR_SEARCH_MODAL)).is_displayed()
