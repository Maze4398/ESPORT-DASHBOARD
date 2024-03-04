import json
#THIS CODE ALLOWS YOU TO GET THE STRING OF CHARACTERS IF THEY DELIMITATED BY A CHARACTER

with open(r'JSON\heroes.json','r',encoding='utf-8') as f:
    data2 = json.load(f)
def generate_name(name):
    parts = name.split('_') #REPLACE _ WITH THE CHARACTER THAT DELIMITATES YOUR STRING OF CHARACTERS
    if len(parts) > 3:
        return parts[3:]
    else:
        return None


for item in data2:
    item['test'] = generate_name(item['name'])

with open(r'E:\ESPORTS ANALYSIS PROJECT\Data_cleaning\data_cleaning\JSON\HEROES.json' , 'w' , encoding='utf-8') as file:
    json.dump(data2, file, indent=4)

print(data2)



