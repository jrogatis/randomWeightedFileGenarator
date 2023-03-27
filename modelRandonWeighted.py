import random
import randonWeighted as rdw
import age_dic
import job_dic
import marital_dic
import education_dic
import creditHolder_dic
import fixed_dics
import housing_dic


def register():
    age = age_dic.age()
    job = job_dic.job()
    marital = marital_dic.maritalRdw()
    education = education_dic.educationslRdw()
    default_credit = fixed_dics.default_credits[random.randint(0, 2)]
    housing = housing_dic.housingRdw()
    loan = fixed_dics.loans[random.randint(0, 2)]
    contact = fixed_dics.contacts[random.randint(0, 1)]
    month = fixed_dics.months[random.randint(0, 9)]
    day_of_week = fixed_dics.day_of_weeks[random.randint(0, 4)]
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
    y = creditHolder_dic.y()

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
