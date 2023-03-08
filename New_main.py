import numpy as np
import random
import pandas as pd

# TODO - Randomized age distribution based on variable given by user
age_distribution_productive_weights = [0.161, 0.149, 0.143, 0.132, 0.115, 0.108, 0.101, 0.091]
age_distribution_productive = ["18-24", "25-29", "30,34", "35-39", "40-44", "45-49", "50-54", "55-59"]
age_distribution_senior = ["60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95-99"]
age_distribution_senior_weights = [0.343, 0.238, 0.160, 0.108, 0.075, 0.047, 0.019, 0.010]
# TODO - Randomized generator of districts based by variables given by user
districts = [
    {"index": 0, "population_share": 0.3, "age_distribution": [66, 34], "urbanization_rate": 0.8, "higher_education_rate": 0.5, "average_income": 87000, "gini index": 0.3},
    {"index": 1, "population_share": 0.2, "age_distribution": [72, 28], "urbanization_rate": 0.6, "higher_education_rate": 0.4, "average_income": 75000, "gini index": 0.3},
    {"index": 2, "population_share": 0.1, "age_distribution": [68, 32], "urbanization_rate": 0.4, "higher_education_rate": 0.3, "average_income": 66000, "gini index": 0.3},
    {"index": 3, "population_share": 0.1, "age_distribution": [77, 23], "urbanization_rate": 0.3, "higher_education_rate": 0.2, "average_income": 45000, "gini index": 0.3},
    {"index": 4, "population_share": 0.05, "age_distribution": [80, 20], "urbanization_rate": 0.2, "higher_education_rate": 0.15, "average_income": 50000, "gini index": 0.3},
    {"index": 5, "population_share": 0.05, "age_distribution": [60, 40], "urbanization_rate": 0.1, "higher_education_rate": 0.1, "average_income": 38000, "gini index": 0.3},
    {"index": 6, "population_share": 0.1, "age_distribution": [70, 30], "urbanization_rate": 0.4, "higher_education_rate": 0.1, "average_income": 40000, "gini index": 0.3},
    {"index": 7, "population_share": 0.1, "age_distribution": [76, 24], "urbanization_rate": 0.7, "higher_education_rate": 0.2, "average_income": 45000, "gini index": 0.3},
    {"index": 8, "population_share": 0.15, "age_distribution": [74, 26], "urbanization_rate": 0.3, "higher_education_rate": 0.4, "average_income": 41000, "gini index": 0.3},
    {"index": 9, "population_share": 0.1, "age_distribution": [72, 28], "urbanization_rate": 0.6, "higher_education_rate": 0.2, "average_income": 58000, "gini index": 0.3}
]


def choose_district():
    return random.choices(districts, weights=[d["population_share"] for d in districts])[0]["index"]


def generate_age(district):
    age_distribution = district['age_distribution']
    age_group = random.choices(['18-59', '60+'], weights=age_distribution)[0]
    if age_group == '18-59':
        age_group = random.choices(age_distribution_productive, weights=age_distribution_productive_weights)[0]
        if age_group[0:2] == '18':
            return 18 + random.randint(0, 6)
        else:
            return int(age_group[0:2]) + random.randint(0, 4)
    elif age_group == '60+':
        age_group = random.choices(age_distribution_senior, weights=age_distribution_senior_weights)[0]
        return int(age_group[0:2]) + random.randint(0, 4)


# TODO - sex disproportion with age
def generate_sex():
    return random.choices(['M', 'F'], weights=[1, 1])[0]


def is_urban(district):
    urbanization = district['urbanization_rate']
    return random.choices([True, False], weights=[urbanization, 1-urbanization])[0]


def generate_education(district, age, urban):
    weight = district["higher_education_rate"]
    if age > 21 & age < 25:
        weight += 0.1
    elif age >= 25:
        weight += 0.2
    if urban:
        weight += 0.3
    return random.choices([True, False], weights=[weight, 1 - weight])[0]


# TODO - sensible (and more random) income distribution
def generate_income(district, age, urban, educated):
    income = district["average_income"]
    r = random.randint(100, 2000)/1200
    income *= r
    if 50 < age < 60:
        income *= (age / 100) * random.randint(1, 2500)/1200
    if educated:
        income *= random.randint(700, 2200)/1200
    if not urban:
        income *= random.randint(300, 1300)/1200
    return income


def create_voters(population):
    voters = pd.DataFrame(columns=['District', 'Age', 'Sex', 'Urban', 'Educated', 'Income'])
    for i in range (0, population):
        voter = create_voter()
        voters.loc[len(voters)] = voter
    return voters


def create_voter():
    district = (choose_district())
    age = generate_age(districts[district])
    sex = generate_sex()
    urban = is_urban(districts[district])
    educated = generate_education(districts[district], age, urban)
    income = round(generate_income(districts[district], age, urban, educated))
    return [district, age, sex, urban, educated, income]


if __name__ == '__main__':
    d = create_voters(500000)
    d.to_csv('voters.csv')
