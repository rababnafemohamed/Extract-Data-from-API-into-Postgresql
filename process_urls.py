
import requests
import pandas as pd

def process_urls(urls):
    dataframes = []
    for url in urls:
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Normalize the JSON data into a DataFrame
                df = pd.json_normalize(data)
                # Append the DataFrame to the list
                dataframes.append(df)
            else:
                # Print error message if the response status is not 200
                print(f"Error: {response.status_code}, {url}")
        except Exception as e:
            # Print error message if an exception occurs
            print(f"Error: {e}")
    return dataframes
