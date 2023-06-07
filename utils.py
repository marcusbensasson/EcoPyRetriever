import json

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
    Prompt the user to enter the name for a filename without the extension.
    """
    file_name = input("Enter the name for the export file (without the extension): ")
    if file_name.endswith('.csv'):
        file_name = file_name[:-4] 
    return file_name

def prompt_for_output_format():
    """
    Prompt the user to enter their desired output format by choosing from a menu.
    Return the chosen format as a string.
    """
    options = ['excel', 'csv']
    print("\nPlease select the desired output format:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Invalid input. Please enter a number from 1 to {len(options)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_dict_to_file(dict_obj, file_path):
    """
    Save a dictionary object to a JSON file.
    
    :param dict_obj: The dictionary object to save
    :param file_path: The path of the file to save the dictionary to
    """
    with open(file_path, 'w') as file:
        json.dump(dict_obj, file, ensure_ascii=False, indent=4)

def load_dict_from_file(file_path):
    """
    Load a dictionary object from a JSON file.
    
    :param file_path: The path of the file to load the dictionary from
    :return: The loaded dictionary object
    """
    with open(file_path, 'r') as file:
        dict_obj = json.load(file)
    return dict_obj
