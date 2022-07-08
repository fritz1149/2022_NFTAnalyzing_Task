import json
import time
import random

def output(file_path, iterable):
    file = open(file_path, "a")
    for item in iterable:
        file.write(str(item) + "\n")
    file.close()
    
def output_json(file_path, data):
    file = open(file_path, "w")
    file.write(json.dumps(data))
    file.close()
    
def input_lines(file_path):
    file = open(file_path, "r")
    ret = file.readlines()
    file.close()
    return ret

def input_json(file_path):
    file = open(file_path, "r")
    ret = json.loads(file.read())
    file.close()
    return ret

def sleep_random(base, scale):
    delta = random.random() * scale
    time.sleep(base + delta)
    
def count_json(file_path):
    file = open(file_path, "r")
    json_list = json.loads(file.read())
    file.close()
    return json_list

if __name__ == "__main__":
    print(len(count_json("../data/tokenURI.json")))