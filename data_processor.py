import os
import eurostat
from utils import save_dict_to_file, load_dict_from_file

class DataProcessor:
    """
    The DataProcessor class is designed to process and pivot raw data obtained from Eurostat API queries.
    """
    
    def make_dicts(self, selected_indicator, query_string):
        """
        Creates a dictionary for the query that can be used to map column labels to more descriptive ones.
        """
        labels = list(query_string.keys())
        print(labels)
        query_dict=dict()

        # Check if a dictionary file already exists for this query
        dict_dir = 'dictionaries'
        dict_file = os.path.join(dict_dir, f"{selected_indicator}.json")
        if os.path.isfile(dict_file):
            # Load the existing dictionary file
            query_dict = load_dict_from_file(dict_file)
        else:
            # Generate a new dictionary and save it to a file
            for par in labels:
                try:
                    par_dict = dict(eurostat.get_dic(selected_indicator, par, full=False))
                    query_dict[par] = par_dict
                except: continue
            # Save the new dictionary to a file
            save_dict_to_file(query_dict, dict_file)

        return query_dict


    def pivot_data(self, raw_data, query_dict):
        """
        Pivot the raw data by setting the 'time' column as the index and combining other relevant columns
        to create new column headers.
        
        :param raw_data: DataFrame containing raw data from the Eurostat API
        :return: DataFrame with the pivoted data
        """
        index_column = 'time'
        value_column = 'values'

        # Determine which columns to use as the new column headers
        data_columns = raw_data.columns.tolist()
        data_columns.remove(index_column)
        data_columns.remove(value_column)
        
    # Create a new column combining the selected data columns
        raw_data['combined_column'] = raw_data[data_columns].apply(
            lambda row: ' - '.join(query_dict[col].get(row[col], row[col]) if col in query_dict and row[col] in query_dict[col] else row[col] for col in data_columns), axis=1)
    
        # Pivot the data using the combined column
        data = raw_data.pivot_table(index=index_column, columns='combined_column', values=value_column)
        # data.index = pd.to_datetime(data.index)
        # data.sort_index(inplace=True)

        return data

    def save_data(self, data, file_name, file_format):
        """
        Save the processed data to a file with the specified file name and format.
        
        :param data: DataFrame containing the processed data
        :param file_name: String with the desired file name (without the extension)
        :param file_format: String with the desired file format ('excel' or 'csv')
        """
        if file_format == 'excel':
            file_path = os.path.join(os.path.expanduser('~'), 'Downloads', f"{file_name}.xlsx")
            data.to_excel(file_path)
        elif file_format == 'csv':
            file_path = os.path.join(os.path.expanduser('~'), 'Downloads', f"{file_name}.csv")
            data.to_csv(file_path)
        else:
            raise ValueError("Invalid file format. Please choose 'excel' or 'csv'.")

        print(f"Data saved to {file_path}")
