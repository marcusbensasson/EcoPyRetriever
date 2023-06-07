from eurostatapiclient import EurostatAPIClient
from eurostat_query_manager import EurostatQueryManager
from data_processor import DataProcessor
from utils import get_file_name, prompt_for_output_format


# Create an instance of the Eurostat API client
client = EurostatAPIClient('1.0', 'json', 'en')

# Instantiate the EurostatQueryManager, fetch the selected dataset, and store it as a DataFrame
query_manager = EurostatQueryManager()
raw_data, selected_indicator, query_string = query_manager.fetch_data(client)

# Pivot the DataFrame to have time as index
data_processor = DataProcessor()
query_dict = data_processor.make_dicts(selected_indicator, query_string)
data = data_processor.pivot_data(raw_data, query_dict)

# Prompt the user for the desired file name and output format, then save the DataFrame to the specified file path
file_name = get_file_name()
output_format = prompt_for_output_format()
data_processor.save_data(data, file_name, output_format)