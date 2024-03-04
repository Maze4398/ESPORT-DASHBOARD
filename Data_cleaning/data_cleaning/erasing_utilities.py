import json

"""
with open('JSON\\heroes.json','r',encoding='utf-8') as f:
    data = json.load(f)

for item in data:
   del item['roles'] #replace test with the column yo want to delete

with open('JSON\\heroes.json','w',encoding='utf-8') as f:
    json.dump(data, f, indent=4)
"""


#-------------------------------------------------------------------------------------------------
#USE THIS CODE IF YOU WANT TO DELETE MULTIPLE COLUMNS


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


json_file = 'JSON\\proPlayers.json'
columns_to_delete = ['profileurl','avatar', 'steamid','avatarmedium','avatarfull','profileirl','last_login','full_history_time','cheese','plus','last_match_time','loccountrycode','fh_unavailable','country_code','is_locked','is_pro','locked_until']  #  with the columns you want to delete
delete_columns_from_json(json_file, columns_to_delete)


