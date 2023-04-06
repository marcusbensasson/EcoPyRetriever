import pandas as pd
from eurostatapiclient import EurostatAPIClient

from eurostat_query_manager import EurostatQueryManager
from data_processor import DataProcessor
from utils import get_file_name


# Create an instance of the Eurostat API client
client = EurostatAPIClient('1.0', 'json', 'en')

# Instantiate the EurostatQueryManager, fetch the selected dataset, and store it as a DataFrame
query_manager = EurostatQueryManager()
raw_data, selected_indicator = query_manager.fetch_data(client)

# Pivot the DataFrame to have time as index
data_processor = DataProcessor()
data = data_processor.pivot_data(raw_data)

# Prompt the user for the desired Excel file name and save the DataFrame to the specified file path
file_name = get_file_name()
data_processor.save_data_to_csv(data, file_name)