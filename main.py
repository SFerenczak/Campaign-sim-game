import random
import pandas as pd


districts = pd.DataFrame({
    'id': pd.Series(dtype='uint8'),
    'pop_share': pd.Series(dtype='float16'),
    'young_share': pd.Series(dtype='float16'),
    'old_share': pd.Series(dtype='float16'),
    'urbanization_rate': pd.Series(dtype='float16'),
    'education_rate': pd.Series(dtype='float16'),
    'avg_income': pd.Series(dtype='int16'),
    'gini_index': pd.Series(dtype='float16')
    })


def generate_districts():
    print(generate_pop_share())
    print()
    #  districts.loc[len(districts)] = [i, '', '', '', '', '', '', '']


def generate_pop_share():
    pop_share = []
    for i in range(0, 11):
        # rolling 3 times to get less dispersed results
        pop_share.append(random.randint(1, 100) + random.randint(1, 100))
    p = sum(pop_share)
    for i in range(0, 11):
        pop_share[i] = pop_share[i]/p
    return pop_share


if __name__ == '__main__':
    generate_districts()
    print(districts)
