class BaseAdvertising:
    advertisers = []

    def __init__(self):
        self.id = None
        self.clicks = 0
        self.views = 0

    def get_clicks(self):
        return self.clicks

    def get_views(self):
        return self.views

    def inc_clicks(self):
        self.clicks += 1

    def inc_views(self):
        self.views += 1

    def describe_me(self):
        print("This class contains basics of both Advertiser and ad classes.")
