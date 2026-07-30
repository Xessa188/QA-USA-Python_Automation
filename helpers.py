import urllib.request

def is_url_reachable(url):
    try:
        response = urllib.request.urlopen(url)
        if response.status == 200:
            return True
        else:
            return False
    except Exception as e:
        return False
