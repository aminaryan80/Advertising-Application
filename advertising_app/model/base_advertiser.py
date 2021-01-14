from abc import ABC


class BaseAdvertising(ABC):
    def __init__(self):
        self.id = None
        self.clicks = 0
        self.views = 0

    def inc_clicks(self):
        self.clicks += 1

    def inc_views(self):
        self.views += 1

    @staticmethod
    def describe_me():
        print("This class contains basics of both Advertiser and ad classes.")
