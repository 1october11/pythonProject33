def thesaurus(*names):
    res = {}
    for name in names:
        el = name[0].capitalize()
        if el not in res:
            res[el] = []
        res[el].append(name)
    return res

print(thesaurus("Иван", "Мария", "Петр", "Илья"))