from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    __total_clicks = 0

    def __init__(self, id, name):
        super().__init__()
        self._id = id
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def help():
        print("\nAdvertiser Fields:\n"
              "id: ID of advertiser\n"
              "name: Name of advertiser\n"
              "click: Total clicks taken by advertiser\n"
              "views: Total views of advertiser ads")

    @staticmethod
    def total_clicks():
        return Advertiser.__total_clicks

    def inc_clicks(self):
        super(Advertiser, self).inc_clicks()
        Advertiser.__total_clicks += 1

    def describe_me(self):
        print("This is Advertiser " + self._name + ".")
