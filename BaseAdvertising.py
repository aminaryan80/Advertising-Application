class BaseAdvertising:
    def __init__(self):
        self._id = None
        self._clicks = 0
        self._views = 0

    @property
    def clicks(self):
        return self._clicks

    @clicks.setter
    def clicks(self, val):
        self._clicks = val

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, val):
        self._views = val

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1

    def describe_me(self):
        print("This class contains basics of both Advertiser and ad classes.")
