import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.urban_routes_url):
            print("Connected to Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        assert pages.get_from_address() == data.address_from
        assert pages.get_to_address() == data.address_to

    def test_select_plan(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        assert pages.get_supportive_plan() == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        pages.click_phone_number()
        pages.write_phone_number(data.phone_number)
        pages.click_next_button()
        pages.write_code(helpers.retrieve_phone_code(self.driver))
        pages.click_confirm()
        assert pages.get_phone_number() == data.phone_number


    def test_fill_card(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        pages.click_phone_number()
        pages.write_phone_number(data.phone_number)
        pages.click_next_button()
        pages.write_code(helpers.retrieve_phone_code(self.driver))
        pages.click_confirm()
        pages.click_payment_method()
        pages.add_card()
        pages.card_number_field(data.card_number)
        pages.card_code_field(data.card_code)
        pages.link_card_button()
        pages.close_payment_method()
        assert pages.get_card_number() == data.card_number
        assert pages.get_card_code() == data.card_code



    def test_message_to_driver_option(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        pages.click_phone_number()
        pages.write_phone_number(data.phone_number)
        pages.click_next_button()
        pages.write_code(helpers.retrieve_phone_code(self.driver))
        pages.click_confirm()
        pages.click_payment_method()
        pages.add_card()
        pages.card_number_field(data.card_number)
        pages.card_code_field(data.card_code)
        pages.link_card_button()
        pages.close_payment_method()
        pages.message_to_driver_field(data.message_for_driver)
        assert pages.get_message_to_driver_field() == data.message_for_driver

    def test_blankets_and_handkerchiefs(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        pages.click_phone_number()
        pages.write_phone_number(data.phone_number)
        pages.click_next_button()
        pages.write_code(helpers.retrieve_phone_code(self.driver))
        pages.click_confirm()
        pages.click_payment_method()
        pages.add_card()
        pages.card_number_field(data.card_number)
        pages.card_code_field(data.card_code)
        pages.link_card_button()
        pages.close_payment_method()
        pages.message_to_driver_field(data.message_for_driver)
        pages.blankets_and_handkerchiefs_slider()
        assert pages.is_blankets_and_handkerchiefs_slider()

    def test_order_2_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        pages.click_phone_number()
        pages.write_phone_number(data.phone_number)
        pages.click_next_button()
        pages.write_code(helpers.retrieve_phone_code(self.driver))
        pages.click_confirm()
        pages.click_payment_method()
        pages.add_card()
        pages.card_number_field(data.card_number)
        pages.card_code_field(data.card_code)
        pages.link_card_button()
        pages.close_payment_method()
        pages.message_to_driver_field(data.message_for_driver)
        pages.blankets_and_handkerchiefs_slider()
        pages.order_2_ice_creams()
        assert pages.ice_cream_count() == "2"

    def test_click_order_button(self):
        self.driver.get(data.urban_routes_url)
        pages = UrbanRoutesPage(self.driver)
        pages.input_from_address(data.address_from)
        pages.input_to_address(data.address_to)
        pages.click_call_a_taxi_button()
        pages.click_supportive_plan_button()
        pages.click_phone_number()
        pages.write_phone_number(data.phone_number)
        pages.click_next_button()
        pages.write_code(helpers.retrieve_phone_code(self.driver))
        pages.click_confirm()
        pages.click_payment_method()
        pages.add_card()
        pages.card_number_field(data.card_number)
        pages.card_code_field(data.card_code)
        pages.link_card_button()
        pages.close_payment_method()
        pages.message_to_driver_field(data.message_for_driver)
        pages.blankets_and_handkerchiefs_slider()
        pages.order_2_ice_creams()
        pages.click_order_button()
        assert pages.car_search_modal()

        @classmethod
        def teardown_class(cls):
            cls.driver.quit()
