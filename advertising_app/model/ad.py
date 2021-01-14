from advertising_app.model.base_advertiser import BaseAdvertising


class Ad(BaseAdvertising):
    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__()
        self.id = id
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.advertiser.inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self.advertiser.inc_views()

    def advertiser(self, advertiser):
        self.advertiser = advertiser

    def describe_me(self):
        print("This is Ad #" + str(self.id))
