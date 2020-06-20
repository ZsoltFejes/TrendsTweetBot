# TweetBot
I started this project to learn more about third party APIs and to learn more about Python.

The script takes the top 10 trending Google Searches and tweets them 5 minuttes before local midnight. It is currently including only GB and US (EDT).
I might add more countries but I see no reason as it just for fun.

Script is running in a docker container, the reason why I chose to deploy it in containerised environment becasue it allows continous development with GitHub actions.

If you want to deploy the container and run it:
```
sudo docker run -it -d --name TweetBot -e CONSUMER_KEY="<CONSUMER_KEY>"  -e CONSUMER_SECRET="<CONSUMER_SECRET>"  -e ACCESS_TOKEN="<ACCESS_TOKEN>"  -e ACCESS_TOKEN_SECRET="<ACCESS_TOKEN_SECRET>" zsoltfejes/tweetbot:latest
```
