number = {'zero': 'ноль','one': 'один','two': 'два','three': 'три','four': 'четыре','five': 'пять','six': 'шесть','seven': 'семь','eight': 'восемь','nine': 'девять','ten': 'десять'}
def  num_translate(num):
    for el, rus in number.items():
        if el == num:
            return rus
        elif el.title() == num:
            return rus.title()
print(num_translate('two'))
print(num_translate('ten'))
print(num_translate('zero'))
print(num_translate('Two'))