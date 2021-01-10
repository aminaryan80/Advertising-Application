from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        BaseAdvertising.advertisers.append(self)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @staticmethod
    def help():
        print("\nAdvertiser Fields:\n" +
              "id: ID of advertiser\n" +
              "name: Name of advertiser\n" +
              "click: Total clicks taken by advertiser\n" +
              "views: Total views of advertiser ads")

    @staticmethod
    def get_total_clicks():
        total_clicks = 0
        for advertiser in BaseAdvertising.advertisers:
            total_clicks += advertiser.get_clicks()
        return total_clicks

    def describe_me(self):
        print("This is Advertiser " + self.name + ".")
