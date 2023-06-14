import pandas as pd
import tkinter as tk
from tkcalendar import DateEntry
import plotly.express as px
from datetime import datetime

# Step 1: Data Retrieval
# Read the CSV files into DataFrames
confirmed_file = "ccse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_file = "ccse_covid_19_time_series/time_series_covid19_deaths_global.csv"
recovered_file = "ccse_covid_19_time_series/time_series_covid19_recovered_global.csv"

confirmed_data = pd.read_csv(confirmed_file)
deaths_data = pd.read_csv(deaths_file)
recovered_data = pd.read_csv(recovered_file)

# Step 2: Data Preprocessing
# Clean and preprocess the data
confirmed_data_cleaned = confirmed_data.drop(['Province/State', 'Lat', 'Long'], axis=1)
deaths_data_cleaned = deaths_data.drop(['Province/State', 'Lat', 'Long'], axis=1)
recovered_data_cleaned = recovered_data.drop(['Province/State', 'Lat', 'Long'], axis=1)

# Step 3: Visualization Design
# Function to create a line chart
def create_line_chart(data, country, start_date, end_date):
    # Convert start_date and end_date to the required format
    start_date_str = start_date.strftime('%m/%d/%y').lstrip("0").replace("/0", "/")
    end_date_str = end_date.strftime('%m/%d/%y').lstrip("0").replace("/0", "/")

    # Filter the data based on country and date range
    country_data = data.query("`Country/Region` == @country")
    country_data_filtered = country_data.loc[:, start_date_str:end_date_str]

    # Transpose the DataFrame so that the dates are in the columns and the cases are in the rows.
    country_data_transposed = country_data_filtered.transpose()

    # Rename the columns so that the cases column is called "Cases".
    country_data_transposed.columns = ['Cases']

    # Reset the index so that the dates are the index again.
    country_data_transposed.reset_index(inplace=True)

    # Rename the index so that it is called "Date".
    country_data_transposed.rename(columns={'index': 'Date'}, inplace=True)

    # Create a line chart using the DataFrame.
    fig = px.line(country_data_transposed, x='Date', y='Cases')

    # Update the layout of the line chart.
    fig.update_layout(title=f"Daily New COVID-19 Cases in {country}")

    # Show the line chart.
    fig.show()



# Step 4: User Interaction
def apply_filters():
    country = country_dropdown.get()
    start_date = start_date_picker.get_date()
    end_date = end_date_picker.get_date()

    # Check if the selected date range is valid
    if start_date <= end_date:
        # Convert start_date and end_date to the required format
        start_date_str = start_date.strftime('%m/%d/%y').lstrip("0").replace("/0", "/")
        end_date_str = end_date.strftime('%m/%d/%y').lstrip("0").replace("/0", "/")

        # Check if the selected start_date is available in the dataset
        if start_date_str not in confirmed_data_cleaned.columns:
            print(f"Data not available for start date: {start_date_str}")
            return

        # Check if the selected end_date is available in the dataset
        if end_date_str not in confirmed_data_cleaned.columns:
            print(f"Data not available for end date: {end_date_str}")
            return

        create_line_chart(confirmed_data_cleaned.groupby('Country/Region').sum(), country, start_date, end_date)
    else:
        print("Invalid date range. Please select a valid range.")



# Create the main application window
window = tk.Tk()
window.title("COVID-19 Dashboard")

# Create dropdown menu for country selection
country_label = tk.Label(window, text="Select a country:")
country_label.pack()

# Get unique country names from the DataFrame
countries = confirmed_data_cleaned['Country/Region'].unique()

country_dropdown = tk.StringVar(window)
country_dropdown.set(countries[0])

country_menu = tk.OptionMenu(window, country_dropdown, *countries)
country_menu.pack()

# Create date picker for start and end date selection
date_label = tk.Label(window, text="Select date range:")
date_label.pack()

start_date_picker = DateEntry(window, width=12, background='darkblue', foreground='white', date_pattern='mm/dd/yy')
start_date_picker.pack()

end_date_picker = DateEntry(window, width=12, background='darkblue', foreground='white', date_pattern='mm/dd/yy')
end_date_picker.pack()

# Create Apply button
apply_button = tk.Button(window, text="Apply Filters", command=apply_filters)
apply_button.pack()

# Step 5: Dashboard Layout
# The line chart will be generated based on the user's selection.

# Run the GUI event loop
window.mainloop()

