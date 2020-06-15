#!/usr/bin/env python
import tweepy
import logging
from config import create_api
import time
from pytrends.request import TrendReq

pytrend = TrendReq()
api = create_api()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#def getSearchTrend():
trendUS = pytrend.trending_searches(pn='united_states')
trendUK = pytrend.trending_searches(pn='united_kingdom')

print(trendUS)
print(trendUK)


#def main():
#    api = create_api()
#    while True:
#       api.update_status("Test tweet from Tweepy Python")

#if __name__ == "__main__":
#    main()
