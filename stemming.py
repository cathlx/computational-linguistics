import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer 
from nltk.stem.snowball import SnowballStemmer 

nltk.download('stopwords')
# nltk.download('punkt')

original = 'prohibition.txt'
# results = 'results.txt'

punctuation_marks = ['.', ',', ':', ';', '!', '?', '-']

with open (original, 'r') as file:
	text = file.read().replace('\n', '')

tokens = word_tokenize(text)
print('tokens: ', tokens)

download_stopwords = stopwords.words('english')
stop_text = [i for i in tokens if i not in download_stopwords]
number_of_not_stopwords = len(stop_text)
print('not stopwords: ', stop_text)

words = [x for x in tokens if x not in punctuation_marks] # исключаем знаки препинания из всех слов (включая связки)
print('all words: ', words)

important_words = [x for x in stop_text if x not in punctuation_marks] # исключаем знаки препинания из важных слов
print('words that count: ', important_words)

deleted_words = len(words) - len(important_words) # сколько слов было удалено
percentage = deleted_words/len(words)*100

tok_sent = sent_tokenize(text)
print('sentences: ', tok_sent)

stemsPorter = []
porter = PorterStemmer()
for w in words: 
	a = w
	w = porter.stem(w)
	if w != '': stemsPorter.append(w)
print('Porter stems: ', stemsPorter)

stems = []
stemmer = SnowballStemmer('english')
for word in words:
	word = stemmer.stem(word)
	if word != '': stems.append(word)
print('Snowball stems: ', stems)

print('{:d} words were deleted. That accounts for {:.2f}% of the text (exluding punctuation marks).'.format(deleted_words, percentage))
words_and_stems = {}
for word in words:
	words_and_stems[word] = porter.stem(word), stemmer.stem(word)

print('Both (porter and snowball): ')
for key, value in words_and_stems.items():
        print(key + ': ' + 'porter -> ' + value[0] + ', ' + 'snowball -> ' + value[1])