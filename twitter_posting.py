import tweepy

api_key = "YOUR_API_KEY"
api_key_secret = "YOUR_API_KEY_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Post a tweet
tweet = "Hello world! 🌍 This tweet was posted using Python & Tweepy. #Python #TwitterAPI"
try:
    api.update_status(status=tweet)
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Error: {e}")
