import json

def convertToJSON(string):
    return json.dumps(string, default = lambda o: o.__dict__, sort_keys=True, indent=4)