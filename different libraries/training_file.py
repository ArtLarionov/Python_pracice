import random

articles = ['a', 'the']
nouns = ['cat', 'dog', 'man', 'woman', 'boy', 'girl']
verbs = ['sang', 'jumped', 'ran', 'came', 'got']
adverbs = ['loudly', 'quietly', 'well', 'badly']

lines = input('Enter a number of lines you want to see: ')

if lines == '' or int(lines) <= 0:
    lines = 5
elif int(lines) > 10:
    lines = 10
else:
    lines = int(lines)

for i in range(lines):
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    choice = random.randint(0, 1)
    if choice == 0:
        print(article, noun, verb, adverb)
    else:
        print(article, noun, verb)
