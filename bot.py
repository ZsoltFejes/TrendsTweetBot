#!/usr/bin/env python
import tweepy
import logging
from config import create_api
import time
from pytrends.request import TrendReq
import pandas as pd
import schedule
import time

pytrend = TrendReq()
api = create_api()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class getSearchTrend():
    def trendUS():
        data = pytrend.trending_searches(pn='united_states')
        return data.shift(periods=1).iloc[1:11].to_csv(header=None)

    def trendUK():
        data = pytrend.trending_searches(pn='united_kingdom')
        return data.shift(periods=1).iloc[1:11].to_csv(header=None)

##############################
######## Twitter API #########
##############################
def tweetUS():
    tweetUS = '[Trends BOT]\nTop 10 #trending searches from #UnitedStates #US\nhttps://trends.google.com/trends/trendingsearches/daily?geo=US\n{}'.format(getSearchTrend.trendUS())
    try:
        tweet = api.update_status(tweetUS)
        logger.info('US Tweeted https://twitter.com/ZsoltFejes/status/{}'.format(tweet.id))
    except Exception as e:
        logger.error("Error sending Tweet\n{}".format(e), exc_info=True)

def tweetGB():
    tweetGB = '[Trends BOT]\nTop 10 #trending searches from #UnitedKingdom #GB #UK #England\nhttps://trends.google.com/trends/trendingsearches/daily?geo=GB\n{}'.format(getSearchTrend.trendUK())
    try:
        tweet = api.update_status(tweetGB)
        logger.info('GB Tweeted https://twitter.com/ZsoltFejes/status/{}'.format(tweet.id))
    except Exception as e:
        logger.error("Error sending Tweet\n{}".format(e), exc_info=True)
##############################
######## Schedulers ##########
##############################
schedule.every().day.at("22:55").do(tweetGB) #UTC
schedule.every().day.at("03:55").do(tweetUS) #UTC

def main():
    logger.info('Application has started')
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
