import json
from difflib import get_close_matches
data = json.load(open('data.json'))

word = input ('Enter word: ')
    if word in data:
        return data[word]
    else:
        return 'none'