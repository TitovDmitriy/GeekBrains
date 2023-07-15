import json
import pickle
import os


def save_json_to_pickle(directory, filename):
    with open(os.path.join(directory, filename), 'r') as json_file:
        data = json.load(json_file)
    with open(os.path.join(directory, filename + '.pickle'), 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
