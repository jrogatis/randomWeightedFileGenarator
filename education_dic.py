import randonWeighted as rdw


def educationslRdw():
    education_levels = [{'NoformalEducation': 6.6},
                        {'ElementarySchoolIncomplete': 17.6},
                        {'HigherEducationComplete': 2.4},
                        {'ElementarySchoolComplete': 38.3},
                        {'HighSchoolComplete': 12.8},
                        {'Unknown': 0},
                        {'ProfessionalCourse': 0},
                        {'HighSchoolIncomplete': 19.7}]

    return rdw.weighted_choice(education_levels)
