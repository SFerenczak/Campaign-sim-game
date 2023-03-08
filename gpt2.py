import numpy as np
import pandas as pd


def middle_or_old(i):
    return 'middle' if i % 3 == 1 else 'old'


# read districts dataframe
districts = pd.read_csv('gpt.csv')


ids = list(range(1, 30000))
district = [i for i in range(1, 11) for j in range(3000)]
sex = ['M' if i % 2 == 0 else 'F' for i in range(30000)]
age_group = ['young' if i % 3 == 0 else middle_or_old(i) for i in range(30000)]
print(age_group)
