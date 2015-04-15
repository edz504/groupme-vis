import simplejson, urllib, urlparse

with open('access_token.data', 'rb') as f:
    token = f.read()

url = 'https://api.groupme.com/v3/groups?token=%s' % token
result = simplejson.load(urllib.urlopen(url))
my_groups = [(g['name'], g['id']) for g in result['response']]

