import randonWeighted as rdw


def maritalRdw():
    maritals = [{"single": 34.7},
                {'married': 46.9},
                {'divorced': 11.9},
                {'unknown': 6.4}]
    return rdw.weighted_choice(maritals)
