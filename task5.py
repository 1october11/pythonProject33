from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    for i in range(n):
        el = choice(nouns)
        el_1 = choice(adverbs)
        el_2 = choice(adjectives)
        joke = "{} {} {}".format(el, el_1, el_2)
        print(joke)
get_jokes(1)
