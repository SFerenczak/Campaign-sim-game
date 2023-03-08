import pandas as pd
import numpy as np

# Making lists with random data for each district
ids = list(range(1, 11))
population_share = np.random.uniform(low=0.1, high=0.5, size=10)
young_share = np.random.uniform(low=0.2, high=0.4, size=10)
old_share = np.random.uniform(low=0.3, high=0.5, size=10)
urbanization_rate = np.random.uniform(low=0.5, high=0.9, size=10)
education_rate = np.random.uniform(low=0.5, high=0.9, size=10)
avg_income = np.random.normal(loc=50000, scale=10000, size=10)
gini_index = np.random.uniform(low=0.2, high=0.6, size=10)

# Making sum of all pop_share = 1
population_share /= population_share.sum()

# Creating dataframe
df = pd.DataFrame({
    'id': ids,
    'population_share': population_share,
    'young_share': young_share,
    'middle_share': 1 - young_share - old_share,
    'old_share': old_share,
    'urbanization_rate': urbanization_rate,
    'education_rate': education_rate,
    'avg_income': avg_income,
    'gini_index': gini_index
})

# Wyświetlenie dataframe
df.to_csv('gpt.csv', index=False)
