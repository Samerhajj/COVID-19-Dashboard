# COVID-19 Dashboard

This COVID-19 Dashboard is a data visualization tool that allows users to explore and analyze the daily new COVID-19 cases for different countries. It provides an interactive interface to select a country and date range, and generates a line chart to visualize the data.

## Features

- Select a country from the dropdown menu.
- Choose a start and end date using the date picker.
- Click the "Apply Filters" button to generate a line chart showing the daily new COVID-19 cases for the selected country and date range.

## Requirements

- Python 3.7 or higher
- pandas
- tkinter
- tkcalendar
- plotly

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Samerhajj/COVID-19-Dashboard.git
   ```

2. Navigate to the project directory:
    ```bash
    cd covid-19-dashboard
    ```


3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Data Source

The data used in this project is provided by [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19).

- `time_series_covid19_confirmed_global.csv`: Contains the daily reported COVID-19 confirmed cases worldwide.
- `time_series_covid19_deaths_global.csv`: Contains the daily reported COVID-19 deaths worldwide.
- `time_series_covid19_recovered_global.csv`: Contains the daily reported COVID-19 recoveries worldwide.






## Usage

1. Run the script `covid_dashboard.py`:

   ```shell
   python covid_dashboard.py
   ```

2. The COVID-19 Dashboard window will open. 
3. Select a country from the dropdown menu.
4. Choose a start and end date using the date picker.
5. Choose a start and end date using the date picker.
6. The line chart will be displayed showing the daily new COVID-19 cases for the selected country and date range.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
    
# Acknowledgements
- The data used in this project is provided by Johns Hopkins University.

