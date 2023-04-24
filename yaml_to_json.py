import yaml
import json

with open('options.yaml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('options.json', 'w') as json_file:
    json.dump(configuration, json_file)
    
output = json.dumps(json.load(open('options.json')), indent=2)
print(output)