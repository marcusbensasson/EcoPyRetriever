# EcoPyExplorer

EcoPyExplorer is a Python tool designed to fetch, process, and export data from the Eurostat API. The tool allows users to select a predefined query from a JSON file, retrieve the relevant data, and save the results as a CSV file. This programme is not so great for browsing Eurostat data (a better name for it would be EcoPyRetriever). Rather, if you have a dataset that you use regularly, this is a quicker way of retrieving it each time.

## Features

- User-friendly selection of predefined queries
- Retrieves data from Eurostat API
- Processes data into a clean, readable format

## Dependencies

- pandas
- eurostatapiclient

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Clone the repository or download the source files.
3. Prepare a JSON file with the query parameters for the desired Eurostat dataset. The JSON file should contain a list of dictionaries, each representing a query. Each dictionary should have the following keys:

   - `query_name`: A user-friendly name for the query.
   - `query_code`: The dataset code for the Eurostat API.
   - `query_string`: A dictionary containing the query parameters (e.g., filters).

4. Run the `main.py` script using a Python interpreter.
5. Follow the prompts to enter the JSON file name (with or without the .json extension), select a query, and specify the output CSV file name (with or without the .csv extension).

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to the developers of the Eurostat API Client library for providing an easy-to-use interface to the Eurostat API.
- This project has also been helped along by use OpenAI's ChatGPT, which has made progress massively faster than it would have been otherwise.
