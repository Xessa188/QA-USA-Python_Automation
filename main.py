import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

        if data.urban_routes_url:
            self.driver.get(data.urban_routes_url)
        else:
            print("Error: urban_routes_url is missing in data.py")

        self.routes_page = UrbanRoutesPage(self.driver)

    # Test Case 1
    def test_set_route(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        time.sleep(1)
        assert self.routes_page.get_from_value() == data.address_from
        assert self.routes_page.get_to_value() == data.address_to

    # Test Case 2
    def test_select_plan(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()
        time.sleep(1)

    # Test Case 3
    def test_fill_phone_number(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()

        self.routes_page.click_phone_button()
        self.routes_page.fill_phone_number(data.phone_number)
        assert self.routes_page.get_phone_field_value() == data.phone_number
        self.routes_page.click_phone_next()
        time.sleep(2)

        sms_token = helpers.retrieve_phone_code(self.driver)
        self.routes_page.enter_sms_code(sms_token)
        self.routes_page.click_sms_confirm()
        time.sleep(1)

    # Test Case 4
    def test_fill_card(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()

        self.routes_page.click_phone_button()
        self.routes_page.fill_phone_number(data.phone_number)
        self.routes_page.click_phone_next()
        sms_token = helpers.retrieve_phone_code(self.driver)
        self.routes_page.enter_sms_code(sms_token)
        self.routes_page.click_sms_confirm()
        time.sleep(1)

        self.routes_page.click_payment_method()
        assert self.routes_page.is_payment_modal_displayed() is True
        self.routes_page.click_add_card()
        self.routes_page.fill_card_details(data.card_number, data.card_code)
        time.sleep(1)
        assert self.routes_page.is_link_button_clickable() is True
        self.routes_page.click_link_card()
        time.sleep(1)
        self.routes_page.close_payment_modal()
        time.sleep(1)
        assert self.routes_page.get_payment_method_text() == "Card"

    # Test Case 5
    def test_comment_for_driver(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()

        self.routes_page.enter_driver_comment(data.message_for_driver)
        assert self.routes_page.get_driver_comment_value() == data.message_for_driver
        time.sleep(1)

    # Test Case 6
    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()

        self.routes_page.toggle_blanket_option()
        assert self.routes_page.is_blanket_property_checked() is True
        time.sleep(1)

    # Test Case 7
    def test_order_2_ice_creams(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()

        self.routes_page.order_ice_creams(2)
        assert self.routes_page.get_ice_cream_count() == "2"
        time.sleep(1)

    # Test Case 8
    def test_car_search_model_appears(self):
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        self.routes_page.click_call_a_taxi_main_button()
        self.routes_page.select_supportive_tariff()

        self.routes_page.click_phone_button()
        self.routes_page.fill_phone_number(data.phone_number)
        self.routes_page.click_phone_next()
        sms_token = helpers.retrieve_phone_code(self.driver)
        self.routes_page.enter_sms_code(sms_token)
        self.routes_page.click_sms_confirm()
        time.sleep(1)

        self.routes_page.click_order_taxi()
        assert self.routes_page.is_car_search_visible() is True

    def teardown_method(self):
        self.driver.quit()
