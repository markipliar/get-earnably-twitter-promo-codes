
import tweepy, re, json

user_info = {
  'consumer_key':         '6XkfEIEcwahq6ri2JK9pGN1JZ',
  'consumer_secret':      '//',
  'access_token':         '431822362-H5DczRp0yPYuyLMdTV0djKBaTBFQQRpEBimFV8Ym',
  'access_token_secret':  '//'
}

auth = tweepy.OAuthHandler(user_info['consumer_key'], user_info['consumer_secret'])
auth.set_access_token(user_info['access_token'], user_info['access_token_secret'])

api = tweepy.API(auth)

public_tweets = api.user_timeline('earnably')
for tweet in public_tweets:
    print(tweet.text + '\n')
    
earn_tweets = list(filter(lambda y: y != "",list(map(lambda x: re.search(r"[A-Z]+\d+",x.text).group(0) if re.search(r"[A-Z]+\d+",x.text) != None else "", public_tweets[0:3]))))

print(earn_tweets)

myfilename = 'registry.json'

with open(myfilename, 'r') as f:
    myjson = json.load(f)
    print(myjson is dict)
    for num in range(len(earn_tweets)):
        if earn_tweets[num] not in myjson['codes']:
            myjson['codes'].append(earn_tweets[num])
    print(myjson)
    
with open(myfilename, 'w') as f:
    json.dump(myjson, f, indent=4)

with open(myfilename, 'r') as f:
    mynewjson = json.load(f)
    print(mynewjson)
