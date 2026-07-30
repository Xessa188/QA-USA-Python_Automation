import data
import helpers


def retrieve_phone_code(driver) -> str:
    """This code retrieves phone confirmation number and returns it as a string.
    Use it when application waits for the confirmation code to pass it into your tests.
    The phone confirmation code can only be obtained after it was requested in application."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No phone confirmation code found.\n"
                            "Please use retrieve_phone_code only after the code was requested in your application.")
        return code


# Checks if Routes is up and running. Do not change
def is_url_reachable(url):
    """Check if the URL can be reached. Pass the URL for Urban Routes as a parameter.
    If it can be reached, it returns True, otherwise it returns False"""

    import ssl
    import urllib.request

    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            # print("Response Status Code:", response.status) #for debugging purposes
            if response.status == 200:
                return True
            else:
                return False
    except Exception as e:
        print(e)


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        pass

    def test_select_plan(self):
        # Add in S8
        pass

    def test_fill_phone_number(self):
        # Add in S8
        pass

    def test_fill_card(self):
        # Add in S8
        pass

    def test_comment_for_driver(self):
        # Add in S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        pass

    def test_order_2_ice_creams(self):
        for i in range(2):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        pass
