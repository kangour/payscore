# -*- coding: utf-8 -*-


class BaseWeChatPayScoreAPI:
    """ WeChat PayScore API base class """

    def __init__(self, client=None):
        self._client = client

    def _get(self, url, **kwargs):
        if getattr(self, "API_BASE_URL", None):
            kwargs["api_base_url"] = self.API_BASE_URL
        return self._client.get(url, **kwargs)

    def _post(self, url, **kwargs):
        if getattr(self, "API_BASE_URL", None):
            kwargs["api_base_url"] = self.API_BASE_URL
        return self._client.post(url, **kwargs)
