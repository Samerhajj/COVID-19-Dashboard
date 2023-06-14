import pandas as pd

# Read the CSV file into a DataFrame
confirmed_file = "ccse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_file = "ccse_covid_19_time_series/time_series_covid19_deaths_global.csv"
recovered_file = "ccse_covid_19_time_series/time_series_covid19_recovered_global.csv"

confirmed_data = pd.read_csv(confirmed_file)
deaths_data = pd.read_csv(deaths_file)
recovered_data = pd.read_csv(recovered_file)
print(confirmed_data.head())
print(deaths_data.head())
print(recovered_data.head())


# Perform data cleaning
confirmed_data_cleaned = confirmed_data.fillna(0)  # Fill missing values with zero
deaths_data_cleaned = deaths_data.fillna(0)
recovered_data_cleaned = recovered_data.fillna(0)

# Calculate daily new cases
confirmed_data_cleaned['daily_new_cases'] = confirmed_data_cleaned.iloc[:, -1].diff()

# Convert 'Country/Region' column to string type
confirmed_data_cleaned['Country/Region'] = confirmed_data_cleaned['Country/Region'].astype(str)
deaths_data_cleaned['Country/Region'] = deaths_data_cleaned['Country/Region'].astype(str)
recovered_data_cleaned['Country/Region'] = recovered_data_cleaned['Country/Region'].astype(str)

# Perform data aggregation by country
confirmed_data_aggregated = confirmed_data_cleaned.groupby('Country/Region').sum(numeric_only=True)
deaths_data_aggregated = deaths_data_cleaned.groupby('Country/Region').sum(numeric_only=True)
recovered_data_aggregated = recovered_data_cleaned.groupby('Country/Region').sum(numeric_only=True)
