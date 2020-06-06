import json
import yaml
import os


def load_file(path_to_file1, path_to_file2):
    dir = os.path.dirname(__file__)
    file1_name = os.path.join(dir, path_to_file1)
    file2_name = os.path.join(dir, path_to_file2)
    file1 = file1_name
    file2 = file2_name
    if os.path.splitext(file1_name)[1] == ".json" and\
            os.path.splitext(file2_name)[1] == ".json":
        file1 = json.load(open(file1_name))
        file2 = json.load(open(file2_name))
    elif os.path.splitext(file1_name)[1] == ".yml" and\
            os.path.splitext(file2_name)[1] == ".yml":
        file1 = yaml.safe_load(open(file1_name))
        file2 = yaml.safe_load(open(file2_name))
    return file1, file2
