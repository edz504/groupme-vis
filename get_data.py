import simplejson, urllib, urlparse, pickle

with open('access_token.data', 'rb') as f:
    token = f.read()

url = 'https://api.groupme.com/v3/groups?token=%s' % token
result = simplejson.load(urllib.urlopen(url))
my_groups = [(g['name'], g['id']) for g in result['response']]
pdt_id = my_groups[1][1]

first = True
while (True):
    if first:
        url = 'https://api.groupme.com/v3/groups/%s/messages?limit=100&token=%s' % (pdt_id, token)
        result = simplejson.load(urllib.urlopen(url))
        pdt_messages = result['response']['messages']
        last_id = result['response']['messages'][len(result['response']['messages']) - 1]['id']
        first = False
    else:
        url = 'https://api.groupme.com/v3/groups/%s/messages?limit=100&before_id=%s&token=%s' % (pdt_id, last_id, token)
        result = simplejson.load(urllib.urlopen(url))

        # check for errors / are we at the end?
        if result['meta']['code'] == 304:
            # we're done 
            break
        pdt_messages += result['response']['messages']
        last_id = result['response']['messages'][len(result['response']['messages']) - 1]['id']

    print "%d / 2283 retrieved" % len(pdt_messages) 

pickle.dump(pdt_messages, open('pdt_2015.p', 'wb'))