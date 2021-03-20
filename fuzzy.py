import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

standard = 'жадина-говядина, соленый огурец, на полу валяется, никто его не ест'

with open('greedy.csv', newline = '', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        item = row['text'].replace('.', '').lower()
        print('Ratio of \'{0}\' and \'{1}\' is {2}.'.format(item, standard, fuzz.ratio(row['text'], standard)))
        print('Partial ratio of \'{0}\' and \'{1}\' is {2}.'.format(item, standard, fuzz.partial_ratio(row['text'], standard)))


