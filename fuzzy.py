import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

standard = 'жадина-говядина, соленый огурец, на полу валяется, никто его не ест'
d = {}

with open('greedy.csv', newline = '', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        item = row['text'].strip().replace('.', '').lower()
        fratio = int(fuzz.ratio(item, standard))
        print('Ratio of \'{0}\' and \'{1}\' is {2}.'.format(item, standard, fratio))
        d[fratio] = d.get(fratio, set()) | set([item])
    for key, values in sorted(d.items(), key = lambda x: -x[0]):
        print(key, values)
