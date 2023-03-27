import random
import randonWeighted as rdw

jobs = ['housemaid',
        'retired',
        'student',
        'management',
        'blue-collar',
        'self-employed',
        'unknown',
        'entrepreneur',
        'services',
        'unemployed',
        'admin.',
        'technician']

maritals = ['single',
            'married',
            'divorced',
            'unknown']

educations = [
    'unknown',
    'basic.9y',
    'university.degree',
    'basic.4y',
    'high.school',
    'illiterate',
    'professional.course',
    'basic.6y']

default_credits = ['no', 'yes', 'unknown']
housings = ['no', 'yes', 'unknown']
loans = ['no', 'yes', 'unknown']

contacts = ['telephone',
            'cellular']

months = [
    'jul',
    'sep',
    'may',
    'mar',
    'jun',
    'aug',
    'oct',
    'nov',
    'dec',
    'apr']

day_of_weeks = [
    'mon',
    'tue',
    'thu',
    'fri',
    'wed']

ys = ['yes', 'no']

header = ['age', 'job', 'marital', 'education',
          'default_credit', 'housing', 'loan', 'contact',
          'month', 'day_of_week', 'duration', 'campaign',
          'pdays', 'previous', 'poutcome', 'emp_var_rate', 'cons_price_idx',
          'cons_conf_idx', 'euribor3m', 'nr_employed', 'y']


def register():
    age = random.randint(18, 99)
    job = jobs[random.randint(0, 11)]
    marital = maritals[random.randint(0, 3)]
    education = educations[random.randint(0, 7)]
    default_credit = default_credits[random.randint(0, 2)]
    housing = housings[random.randint(0, 2)]
    loan = loans[random.randint(0, 2)]
    contact = contacts[random.randint(0, 1)]
    month = months[random.randint(0, 9)]
    day_of_week = day_of_weeks[random.randint(0, 4)]
    duration = random.randint(0, 999)
    campaign = random.randint(1, 2)
    pdays = 999
    previous = random.randint(1, 999)
    poutcome = 'nonexistent'
    emp_var_rate = '1.1'
    cons_price_idx = '93.994'
    cons_conf_idx = '-36.4'
    euribor3m = '4.857'
    nr_employed = 5191
    y = ys[random.randint(0, 1)]

    data = [age,
            job,
            marital,
            education,
            default_credit,
            housing,
            loan,
            contact,
            month,
            day_of_week,
            duration,
            campaign,
            pdays,
            previous,
            poutcome,
            emp_var_rate,
            cons_price_idx,
            cons_conf_idx,
            euribor3m,
            nr_employed,
            y
            ]
    return data
