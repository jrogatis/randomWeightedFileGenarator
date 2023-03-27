import randonWeighted as rdw


def housingRdw():
    housings = [{'no': 30}, {'yes': 68}, {'unknown': 2}]

    return rdw.weighted_choice(housings)
