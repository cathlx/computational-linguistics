import collections

def tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

d = {}
with open('sherlock.txt', encoding = 'utf-8') as file:
  text = file.read().replace('\n', '').replace('!', '.').replace('?', '.').replace('...', '.')
  for sentence in text.split('.'):
      d[sentence] = len([x for x in sentence.split() if len(x) == 1])  
sentences, words = text.count('.'), len(text.split(' '))
print('Average sentence length:', '%.3f'%(words/sentences))

s = sorted(d.items(), key = lambda x: -x[1])
print('\'{0}\' contains {1} one-character words(max).'.format(s[0][0], s[0][1]))

with open('sherlock.txt', encoding = 'utf-8') as file:
  a = [word for word in file.read().replace('\n', '').split()]
f = input('Enter the word to calculate frequency: ')      
print('Frequency is {:.3f}'.format(tf(a)[f]))