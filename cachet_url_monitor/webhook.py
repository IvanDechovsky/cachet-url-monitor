from typing import Dict

import requests


class Webhook:
    url: str
    verify: bool or str
    params: Dict[str, str]
    json: Dict[str, str]

    def __init__(self, url: str, params: Dict[str, str], json: Dict[str, str], verify=True):
        self.url = url
        self.params = params
        self.verify = verify
        self.json = json

    def push_incident(self, title: str, message: str):
        format_args = {"title": title, "message": message or title}
        # Interpolate URL and params
        url = self.url.format(**format_args)
        params = {name: str(value).format(**format_args) for name, value in self.params.items()}
        json = {name: str(value).format(**format_args) for name, value in self.json.items()}
        verify = self.verify

        return requests.post(url, params=params, json=json, verify=verify)
