import json
import os

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    else:
        return []

def save_data(data, file_name):
    with open(file_name, "w") as f:
        json.dump(data, f)
