# import requests
# from bs4 import BeautifulSoup
#
# def thirty_year_rainful(city_name)
# url = "https://www.weather.gov/ffc/rainfall_scorecard"
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     # Find all tables on the page
#     tables = soup.find_all('table')
#     for table in tables:
#
import requests
from bs4 import BeautifulSoup


# Function to get rainfall data for a specific city
def get_rainfall_data(city_name):
    url = "https://www.weather.gov/ffc/rainfall_scorecard"
    response = requests.get(url)
    print("hi")

    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the tables on the page
        rainfall_data = soup.find_all('table')
        print(soup.find_all('table'))
        print("hii")
        # Iterate through the tables and look for the data
        print(rainfall_data)
        for table in rainfall_data:
            print("hiii")
            # Search for rows in the table
            rows = table.find_all('tr')
            print("hiii")
            for row in rows:
                # Check if the row contains the city name
                columns = row.find_all('td')
                print("hiiii")
                if columns and city_name.lower() in columns[0].get_text().lower():
                    # Assuming the "Thirty Year Average" row and "Total" column are in specific places
                    thirty_year_avg = None
                    total_column = None

                    # Loop through columns to find specific data
                    for i, col in enumerate(columns):
                        if '30 yr avg' in col.get_text():
                            thirty_year_avg = columns[i + 1].get_text().strip()  # Get value from next column
                        if 'Total' in col.get_text():
                            total_column = columns[i + 1].get_text().strip()  # Get value from next column

                    # Print the relevant data if found
                    if thirty_year_avg and total_column:
                        print(f"City: {city_name}")
                        print(f"30 yr avg: {thirty_year_avg}")
                        print(f"Total: {total_column}")
                    else:
                        print("Could not find the necessary data for this city.")
                    break
            else:
                continue
            break
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


# Input city name from user
city_name = input("Enter city name: ")
get_rainfall_data(city_name)
