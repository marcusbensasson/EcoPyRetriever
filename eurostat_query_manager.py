import json
from utils import promptForJsonFile

class EurostatQueryManager:
    """
    A class to manage Eurostat API queries, including loading queries from a JSON file,
    user query selection, and data retrieval.
    """
    def __init__(self, paramsFile=None):
        """
        Initialize the QueryBuilder with an optional JSON file name. If no file name is provided,
        the user will be prompted to enter one.
        """
        if paramsFile is None:
            paramsFile = promptForJsonFile()
        self.paramsFile = paramsFile
        self.queries = self.loadQueriesFromFile()

    def loadQueriesFromFile(self):
        """
        Load queries from the JSON file specified in the paramsFile attribute.
        Return the parsed JSON content as a list of dictionaries.
        """
        with open(self.paramsFile, 'r') as file:
            queries = json.load(file)
        return queries

    def selectQuery(self):
        """
        Display the query names with numbers and prompt the user to select one.
        Return the "query_code" as a string and the "query-string" dictionary of the selected query.
        """
        print("Please select a query:")
        for i, query in enumerate(self.queries, 1):
            print(f"{i}. {query['query_name']}")

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(self.queries):
                    break
                else:
                    print("Invalid input. Please enter a number from 1 to", len(self.queries))
            except ValueError:
                print("Invalid input. Please enter a number.")

        selectedIndicator = self.queries[choice - 1]['query_code']
        selectedQuery = self.queries[choice - 1]['query_string']
        return selectedIndicator, selectedQuery 
    
    def getDatasetAsDataFrame(self, client):
        """
        Retrieve the dataset from the Eurostat API using the selected query and convert it to a DataFrame.
        """
        selected_indicator, selected_query_string = self.selectQuery()
        query = client.get_dataset(selected_indicator, params=selected_query_string)
        return query.to_dataframe()
    
    def fetch_data(self, client):
        """
        Retrieve the dataset from the Eurostat API using the selected query and convert it to a DataFrame.
        Return the DataFrame and the selected indicator.
        """
        selected_indicator, selected_query_string = self.selectQuery()
        query = client.get_dataset(selected_indicator, params=selected_query_string)
        return query.to_dataframe(), selected_indicator
