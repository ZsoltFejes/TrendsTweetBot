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
        return data.shift(periods=1).iloc[1:4].to_csv(header=None)

    def trendUK():
        data = pytrend.trending_searches(pn='united_kingdom')
        return data.shift(periods=1).iloc[1:4].to_csv(header=None)

##############################
######## Twitter API #########
##############################
def tweet():
    try:
        logger.info('Test tweet from Tweepy Python\n' + getSearchTrend.trendUS())
        api.update_status('Test tweet from Tweepy Python\n' + getSearchTrend.trendUS())
    except Exception as e:
        logger.error("Error sending API request", exc_info=True)
        raise e

##############################
######## Schedulers ##########
##############################
schedule.every(5).minutes.do(tweet)

def main():
    logger.info('Application has started')
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
