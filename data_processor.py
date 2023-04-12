import os
import pandas as pd

class DataProcessor:
    """
    The DataProcessor class is designed to process and pivot raw data obtained from Eurostat API queries.
    """

    def pivot_data(self, raw_data):
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
        raw_data['combined_column'] = raw_data[data_columns].apply(lambda x: ' - '.join(x.astype(str)), axis=1)

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
