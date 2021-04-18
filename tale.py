# coding: utf-8
from utg import relations as r
from utg import logic
from utg import data
from utg import dictionary
from utg import words
from utg import templates
from utg import constructors

games_word = words.Word(type = r.WORD_TYPE.NOUN,
                        forms = [ u'игра', u'игры', u'игре', u'игру', u'игрой', u'игре',    
                                u'игры', u'игр', u'играми', u'игры', u'играми', u'играх',  
                                u'игры', u'игр', u'играм', u'игры', u'играми', u'играх'], 
                        properties = words.Properties(r.ANIMALITY.INANIMATE, r.GENDER.FEMININE))

action_word = words.Word(type = r.WORD_TYPE.VERB,
                         forms = [u'дать', u'дал', u'дало', u'дала', u'дали'] + [u''] * (len(data.WORDS_CACHES[r.WORD_TYPE.VERB]) - 5),
                         properties = words.Properties(r.ASPECT.PERFECTIVE, r.VOICE.DIRECT) )
action_word.autofill_missed_forms() 

test_dictionary = dictionary.Dictionary(words = [games_word, action_word])

template = templates.Template()

template.parse(u'[Npc] [дал|npc] [hero|дт] [games] [игра|games|вн].', externals = ('hero', 'npc', 'games'))

hero = words.WordForm(words.Word(type = r.WORD_TYPE.NOUN,
                                 forms = [u'герой', u'героя', u'герою', u'героя', u'героем', u'герое',
                                        u'герои', u'героев', u'героям', u'героев', u'героями', u'героях',
                                        u'герои', u'героев', u'героям', u'героев', u'героями', u'героях'],
                                 properties = words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.MASCULINE)))

npc = words.WordForm(words.Word(type = r.WORD_TYPE.NOUN,
                                forms = [u'кошка', u'кошки', u'кошке', u'кошку', u'кошкой', u'кошке',
                                       u'кошки', u'кошек', u'кошкам', u'кошек', u'кошками', u'кошках',
                                       u'кошки', u'кошек', u'кошкам', u'кошек', u'кошками', u'кошках'],
                                 properties = words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.FEMININE)))

result = template.substitute(externals = {'hero': hero,
                                        'npc': npc,
                                        'games': constructors.construct_integer(125)},
                             dictionary = test_dictionary)
print(result)
