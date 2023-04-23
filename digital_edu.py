#создай здесь свой индивидуальный проект!
import pandas as pd 

df = pd.read_csv('train.csv')

df = df[['id','sex','has_photo',
         'has_mobile','followers_count','graduation',
         'education_form','education_status','langs',
         'occupation_type','career_start',
         'career_end']]

def langs_to_int(lang_list):
    count = 0
    lang_list = lang_list.split(';')
    for lang in lang_list:
        count += 1
    return count

df['langs'] = df['langs'].apply(langs_to_int)

df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'])
df.drop('education_form',axis=1,inplace=True)


def edu_status(row):
    stat_code = {
        'Alumnus (Specialist)'      : 4,
        'Student (Specialist)'      : 3,
        'Student (Bachelor\'s)'     : 1,
        'Alumnus (Bachelor\'s)'     : 2,
        'Alumnus (Master\'s)'       : 6,
        'PhD'                       : 8,
        'Student (Master\'s)'       : 5,
        'Undergraduate applicant'   : 0,
        'Candidate of Sciences'     : 7,
    }
    return stat_code[row]

df['education_status'] = df['education_status'].apply(edu_status)

'''Команды для анализа имеющихся данных во время оценки'''
print(df.info())
# print(df.sample(10))
# print(df['education_status'].value_counts())
# print(df['langs'].unique())