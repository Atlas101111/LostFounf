import requests


class Http:
    @classmethod
    def get(cls, url, return_json=True):   # get json data from given url
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
