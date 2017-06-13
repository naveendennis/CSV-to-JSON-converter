import csv
import configparser
import json
import os


def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['twitter']
    make_dir(config['target_directory'])
    with open(config['filename'], 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list()
        for current_data in reader:
            current_row = dict()
            for each_key, each_element in zip(headers, current_data):
                current_row[each_key] = each_element
            data.append(current_row)
        result = dict()
        result['data'] = data
    with open(os.path.join(config['target_directory'], config['target_filename']), 'w') as f:
        json.dump(result, f)
