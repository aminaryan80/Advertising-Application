from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):
    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__()
        self._id = id
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self._advertiser.inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self._advertiser.inc_views()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, url):
        self._img_url = url

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    def advertiser(self, advertiser):
        self._advertiser = advertiser

    def describe_me(self):
        print("This is Ad #" + str(self._id))
