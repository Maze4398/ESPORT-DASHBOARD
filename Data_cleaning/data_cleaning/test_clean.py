import json


def delete_columns_from_json(json_file, columns_to_delete):
    # Read the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Delete specified columns
    for item in data:
        for column in columns_to_delete:
            if column in item:
                del item[column]

    # Write the modified data back to the file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


json_file = r'E:\ESPORTS ANALYSIS PROJECT\Data_cleaning\data_cleaning\JSON\leagues.json'
columns_to_delete = ['ticket', 'banner']  #  with the columns you want to delete
delete_columns_from_json(json_file, columns_to_delete)
