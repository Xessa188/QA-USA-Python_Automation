from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    # Locators
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_A_TAXI_MAIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button round')]")

    SUPPORTIVE_TARIFF_BUTTON = (By.XPATH, "//div[text()='Supportive']")
    SUPPORTIVE_TARIFF_CARD_ACTIVE = (By.XPATH, "//div[contains(@class, 't_supportive') and contains(@class, 'active')]")

    PHONE_BUTTON = (By.CLASS_NAME, 'np-button')
    PHONE_INPUT_FIELD = (By.ID, 'phone')
    PHONE_NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    SMS_CODE_FIELD = (By.ID, 'code')
    SMS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button')
    PAYMENT_METHOD_TEXT = (By.CLASS_NAME, 'pp-value_text')
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_FIELD = (By.ID, 'number')
    CARD_CVV_FIELD = (By.ID, 'code')
    CARD_MODAL_TITLE = (By.XPATH, "//div[text()='Add a card']")
    LINK_CARD_BUTTON = (By.XPATH, "//button[text()='Link']")
    CLOSE_PAYMENT_MODAL = (By.XPATH, "//div[@class='payment-picker open']//button[@class='close-button']")

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

    # Actions & Getters
    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_value(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    def get_to_value(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def click_call_a_taxi_main_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CALL_A_TAXI_MAIN_BUTTON))
        self.driver.find_element(*self.CALL_A_TAXI_MAIN_BUTTON).click()

    def select_supportive_tariff(self):
        tariff_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUPPORTIVE_TARIFF_BUTTON))
        is_active = len(self.driver.find_elements(*self.SUPPORTIVE_TARIFF_CARD_ACTIVE)) > 0
        if not is_active:
            self.driver.execute_script("arguments[0].click();", tariff_btn)

    def click_phone_button(self):
        phone_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PHONE_BUTTON))
        self.driver.execute_script("arguments[0].click();", phone_btn)

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_INPUT_FIELD).send_keys(phone_number)

    def get_phone_field_value(self):
        return self.driver.find_element(*self.PHONE_INPUT_FIELD).get_attribute('value')

    def click_phone_next(self):
        self.driver.find_element(*self.PHONE_NEXT_BUTTON).click()

    def enter_sms_code(self, sms_code):
        self.driver.find_element(*self.SMS_CODE_FIELD).send_keys(sms_code)

    def click_sms_confirm(self):
        self.driver.find_element(*self.SMS_CONFIRM_BUTTON).click()

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()

    def fill_card_details(self, card_num, cvv_code):
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_num)
        cvv_element = self.driver.find_element(*self.CARD_CVV_FIELD)
        cvv_element.send_keys(cvv_code)
        cvv_element.send_keys(Keys.TAB)
        self.driver.find_element(*self.CARD_MODAL_TITLE).click()

    def is_link_button_clickable(self):
        return self.driver.find_element(*self.LINK_CARD_BUTTON).is_enabled()

    def click_link_card(self):
        self.driver.find_element(*self.LINK_CARD_BUTTON).click()

    def close_payment_modal(self):
        self.driver.find_element(*self.CLOSE_PAYMENT_MODAL).click()

    def get_payment_method_text(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_TEXT).text

    def enter_driver_comment(self, comment_text):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment_text)

    def get_driver_comment_value(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_attribute('value')

    def toggle_blanket_option(self):
        self.driver.find_element(*self.BLANKET_TOGGLE_SWITCH).click()

    def is_blanket_property_checked(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX_STATUS).get_property('checked')

    def order_ice_creams(self, count):
        for _ in range(count):
            self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER_VALUE).text

    def click_order_taxi(self):
        self.driver.find_element(*self.ORDER_TAXI_BUTTON).click()

    def is_car_search_visible(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CAR_SEARCH_MODAL))
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()
