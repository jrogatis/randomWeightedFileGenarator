import randonWeighted as rdw


def job():
    occupation_distribution = {'Housemaid': 0.9,
                               'Retired': 7.6,
                               'Student': 2.8,
                               'Management': 3.5,
                               'Blue-collar': 20.3,
                               'Self-employed': 11.7,
                               'Unknown': 0.2,
                               'Entrepreneur': 2.0,
                               'Services': 12.1,
                               'Unemployed': 14.3,
                               'Admin.': 4.4,
                               'Technician': 9.9}
    return rdw.weighted_choice(occupation_distribution)
