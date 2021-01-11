from ad import Ad
from advertiser import Advertiser
from base_advertiser import BaseAdvertising

base_advertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img_url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img_url2", "link2", advertiser2)
base_advertising.describe_me()
ad2.describe_me()
advertiser1.describe_me()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()
print("Name of advertiser2: " + advertiser2.name)
advertiser2.name = "New name"
print("Name of advertiser2: " + advertiser2.name)
print("Clicks of ad1: " + str(ad1.clicks))
print("Clicks for advertiser2: " + str(advertiser2.clicks))
print("Total clicks for Advertisers: " + str(Advertiser.total_clicks()))
Advertiser.help()
