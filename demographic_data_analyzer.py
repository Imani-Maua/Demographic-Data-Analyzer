import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_df = df[df['sex'] == 'Male']
    average_age_men = round(men_df['age'].mean(), 1)
    

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == "Bachelors").mean()*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?



    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich =round((higher_education['salary'] == '>50K').mean()*100, 1 )
    lower_education_rich = round((lower_education['salary'] == '>50K').mean()*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
# First of all, create a dataframe for the people who work these number of hours

    num_min_workers = df[df['hours-per-week'] == min_work_hours]

# Then calculate the percentage of these people who work these hours

    rich_percentage = round((num_min_workers['salary'] == '>50K').mean()*100,1)

    # What country has the highest percentage of people that earn >50K?
    total_per_country = df['native-country'].value_counts()
    high_earners = df[df['salary'] == '>50K']
    high_earners_per_country = high_earners['native-country'].value_counts()
    percentage_high_earners = (high_earners_per_country/total_per_country)*100
    highest_earning_country = percentage_high_earners.idxmax()
    highest_earning_country_percentage = round(percentage_high_earners.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_top_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupation_count = india_top_earners['occupation'].value_counts()
    top_IN_occupation = occupation_count.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()