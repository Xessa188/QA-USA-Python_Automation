import time
from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_complete_taxi_booking_flow(self):
        # 1. Addresses entry & value validation assertions
        self.routes_page.enter_from_location(data.address_from)
        self.routes_page.enter_to_location(data.address_to)
        time.sleep(3)
        assert self.routes_page.get_from_value() == data.address_from
        assert self.routes_page.get_to_value() == data.address_to

        # 2. Open up expanded menu panels
        self.routes_page.click_call_a_taxi_main_button()
        time.sleep(2)

        # 3. Supportive Plan tariff panel selection
        self.routes_page.select_supportive_tariff()
        time.sleep(1)

        # 4. Phone input and SMS code confirmation loops
        self.routes_page.click_phone_button()
        self.routes_page.fill_phone_number(data.phone_number)
        assert self.routes_page.get_phone_field_value() == data.phone_number
        self.routes_page.click_phone_next()
        time.sleep(1)

        sms_token = helpers.retrieve_phone_code(self.driver)
        self.routes_page.enter_sms_code(sms_token)
        self.routes_page.click_sms_confirm()
        time.sleep(1)

        # 5. Financial profile linking & clickability verification
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.fill_card_details(data.card_number, data.card_code)
        time.sleep(1)

        assert self.routes_page.is_link_button_clickable() is True
        self.routes_page.click_link_card()
        time.sleep(1)
        self.routes_page.close_payment_modal()
        time.sleep(1)
        assert self.routes_page.get_payment_method_text() == "Card"

        # 6. Messaging documentation validation
        self.routes_page.enter_driver_comment(data.message_for_driver)
        assert self.routes_page.get_driver_comment_value() == data.message_for_driver
        time.sleep(1)

        # 7. Item check via .get_property('checked')
        self.routes_page.toggle_blanket_option()
        assert self.routes_page.is_blanket_property_checked() is True
        time.sleep(1)

        # 8. Counter total loops verification
        self.routes_page.order_ice_creams(2)
        assert self.routes_page.get_ice_cream_count() == "2"
        time.sleep(1)

        # 9. Search interface manifestation overlay confirmation
        self.routes_page.click_order_taxi()
        assert self.routes_page.is_car_search_visible() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
