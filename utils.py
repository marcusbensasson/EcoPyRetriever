"""
Utility functions for user input prompts and other miscellaneous tasks.
"""

def promptForJsonFile():
    """
    Prompt the user to enter the JSON file name without the .json extension. 
    If the user enters 'quit', the program will exit. Otherwise, the function will
    keep asking for a valid file name until one is provided.
    """
    while True:
        fileName = input("Enter the name of the JSON file containing the queries (without the .json extension), or type 'quit' to exit: ")
        if fileName.lower() == 'quit':
            print("Exiting the program.")
            exit()

        if not fileName.endswith('.json'):
            fileName = f"{fileName}.json"
        try:
            with open(fileName, 'r') as file:
                return fileName
        except FileNotFoundError:
            print(f"File '{fileName}' not found. Please try again.")

def get_file_name():
    """
    Prompt the user to enter the name for the CSV file without the extension.
    """
    file_name = input("Enter the name for the CSV file (without the extension): ")
    if file_name.endswith('.csv'):
        file_name = file_name[:-4] 
    return file_name