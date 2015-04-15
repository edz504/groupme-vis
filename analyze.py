import pickle

messages = pickle.load(open('pdt_2015.p', 'rb'))

num_likes = [len(m['favorited_by']) for m in messages]

# most-like message
print messages[num_likes.index(max(num_likes))]