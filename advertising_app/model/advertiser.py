from advertising_app.model.base_advertiser import BaseAdvertising


class Advertiser(BaseAdvertising):
    __total_clicks = 0

    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name

    def inc_clicks(self):
        super(Advertiser, self).inc_clicks()
        Advertiser.__total_clicks += 1

    def describe_me(self):
        print("This is Advertiser " + self.name + ".")

    @staticmethod
    def help():
        print("\nAdvertiser Fields:\n"
              "id: ID of advertiser\n"
              "name: Name of advertiser\n"
              "click: Total clicks taken by advertiser\n"
              "views: Total views of advertiser ads")

    @classmethod
    def total_clicks(cls):
        return cls.__total_clicks
