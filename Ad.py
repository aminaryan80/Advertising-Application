from BaseAdvertising import BaseAdvertising


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

    def get_title(self):
        return self.title

    def get_img_url(self):
        return self.img_url

    def get_link(self):
        return self.link

    def set_title(self, title):
        self.title = title

    def set_img_url(self, url):
        self.img_url = url

    def set_link(self, link):
        self.link = link

    def set_advertiser(self, advertiser):
        self.advertiser = advertiser

    def describe_me(self):
        print("This is Ad #" + str(self.id))
