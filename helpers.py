def is_url_reachable(url):
    import urllib.request
    import ssl

    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            if response.status == 200:
                return True
            else:
                return False
    except Exception as e:
        return False
